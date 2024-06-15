import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
from openai import OpenAI
import os
import threading
import logging
import time

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
logging.info(f"OpenAI API Key set: {'Yes' if os.getenv('OPENAI_API_KEY') else 'No'}")

# Replace 'your-assistant-id' with your actual assistant ID
ASSISTANT_ID = 'asst_8m20MnOFZZdSAcl07IfLgTgg'


def stream_response(notes):
    try:
        update_status("Creating thread...")
        thread = client.beta.threads.create()

        update_status("Adding message to thread...")
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=f"\n\n{notes}"
        )

        update_status("Running assistant...")
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=ASSISTANT_ID
        )

        while True:
            update_status("Checking run status...")
            run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
            if run_status.status == 'completed':
                break
            elif run_status.status == 'failed':
                raise Exception("Assistant run failed")
            time.sleep(1)  # Wait for a second before checking again

        update_status("Retrieving messages...")
        messages = client.beta.threads.messages.list(thread_id=thread.id)

        # Assuming the last message is the assistant's response
        assistant_message = next((m for m in reversed(messages.data) if m.role == 'assistant'), None)

        if assistant_message:
            summary = assistant_message.content[0].text.value
            update_response_area(summary)
            logging.debug(f"Retrieved summary: {summary[:100]}...")  # Log first 100 chars
        else:
            raise Exception("No response from assistant")

        update_status("Done")
    except Exception as e:
        logging.error(f"Error in stream_response: {e}")
        update_response_area(f"Error: {str(e)}")
        update_status("Error")


def update_response_area(content):
    app.after(0, lambda: response_area.delete("1.0", tk.END))
    app.after(0, lambda: response_area.insert(tk.END, content))


def update_status(status):
    app.after(0, lambda: status_label.config(text=f"Status: {status}"))


def submit_notes():
    notes = text_area.get("1.0", tk.END).strip()
    logging.debug(f"Submit button clicked. Notes length: {len(notes)}")
    if notes:
        response_area.delete("1.0", tk.END)
        update_status("Processing...")

        thread = threading.Thread(target=stream_response, args=(notes,))
        thread.start()
        logging.debug("Thread started")
    else:
        logging.warning("No notes entered")
        messagebox.showwarning("Warning", "Please enter some notes to summarize.")
        update_status("Idle")


def clear_text():
    text_area.delete("1.0", tk.END)
    response_area.delete("1.0", tk.END)
    update_status("Idle")
    logging.debug("Cleared all text areas")


# GUI setup
app = tk.Tk()
app.title("Note-Taking App")
app.geometry("800x700")  # Increased height to accommodate new widgets

# Create a text area for note taking
text_area = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=80, height=10)
text_area.pack(padx=10, pady=10)

# Button frame
button_frame = tk.Frame(app)
button_frame.pack(pady=10)

# Create a submit button
submit_button = tk.Button(button_frame, text="Submit", command=submit_notes)
submit_button.pack(side=tk.LEFT, padx=10)

# Create a clear button
clear_button = tk.Button(button_frame, text="Clear", command=clear_text)
clear_button.pack(side=tk.LEFT, padx=10)

# Status indicator
status_label = tk.Label(app, text="Status: Idle", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_label.pack(fill=tk.X, padx=10, pady=5)

# Create a text area for displaying AI response
response_area = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=80, height=10)
response_area.pack(padx=10, pady=10)

# Initialize status
update_status("Idle")

# Start the GUI event loop
app.mainloop()