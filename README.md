# AI-Powered Note Summarizer
This README provides a comprehensive guide for users who want to set up and use your application. It covers all the essential aspects:

1. An overview of what the app does.
2. Key features.
3. Prerequisites and installation instructions.
4. How to use the application.
5. Troubleshooting tips.
6. Information on how to contribute.
7. Licensing information.
8. Acknowledgements.
9. Contact information.



## Overview

The AI-Powered Note Summarizer is a desktop application that leverages OpenAI's advanced language models to automatically summarize your notes. Built with Python and Tkinter, this app provides a user-friendly interface for inputting your notes and receiving concise summaries, making it easier to review and understand lengthy information.

## Features

- Simple and intuitive graphical user interface
- Utilizes OpenAI's Assistants API for high-quality summarization
- Real-time status updates during the summarization process
- Easy-to-use clear functionality to start new summarization tasks
- Detailed logging for debugging and monitoring

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your system
- An OpenAI API key (You'll need to sign up at [OpenAI](https://openai.com) if you haven't already)
- A custom OpenAI Assistant created for summarization (Instructions below)

## Installation

1. Clone this repository to your local machine: git clone https://github.com/CrewRiz/Study-Buddy.git
cd ai-note-summarizer
2. Install the required dependencies: pip install openai
3. Set up your OpenAI API key as an environment variable:
- On Windows:
  ```
  setx OPENAI_API_KEY "your-api-key-here"
  ```
- On macOS/Linux:
  ```
  export OPENAI_API_KEY="your-api-key-here"
  ```

4. Create a custom OpenAI Assistant:
- Go to the [OpenAI platform](https://platform.openai.com/assistants) and sign in.
- Click on "Create assistant" and follow the prompts to create a new assistant.
- Make sure to enable the "Text Summarization" skill for your assistant.
- Once created, note down the Assistant ID.

5. Update the `ASSISTANT_ID` in the `app.py` file with your Assistant ID:
```python
ASSISTANT_ID = 'your-assistant-id-here'


## Overview

Study Buddy is a desktop application that leverages OpenAI's advanced language models to automatically summarize your notes. Built with Python and Tkinter, this app provides a user-friendly interface for inputting your notes and receiving concise summaries, making it easier to review and understand lengthy information.

## Features

- Simple and intuitive graphical user interface
- Utilizes OpenAI's Assistants API for high-quality summarization
- Real-time status updates during the summarization process
- Easy-to-use clear functionality to start new summarization tasks
- Detailed logging for debugging and monitoring

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your system
- An OpenAI API key (You'll need to sign up at [OpenAI](https://openai.com) if you haven't already)
- A custom OpenAI Assistant created for summarization (Instructions below)

## Installation

1. Clone this repository to your local machine:
git clone https://github.com/your-username/ai-note-summarizer.git
cd ai-note-summarizer
Copy
2. Install the required dependencies:
pip install openai
Copy
3. Set up your OpenAI API key as an environment variable:
- On Windows:
  ```
  setx OPENAI_API_KEY "your-api-key-here"
  ```
- On macOS/Linux:
  ```
  export OPENAI_API_KEY="your-api-key-here"
  ```

4. Create a custom OpenAI Assistant:
- Go to the [OpenAI platform](https://platform.openai.com/assistants) and sign in.
- Click on "Create assistant" and follow the prompts to create a new assistant.
- Make sure to enable the "Text Summarization" skill for your assistant.
- Once created, note down the Assistant ID.

5. Update the `ASSISTANT_ID` in the `app.py` file with your Assistant ID:
```python
ASSISTANT_ID = 'your-assistant-id-here'
Usage

Run the application:
Copypython app.py

The application window will open. You'll see two text areas:

The top text area is for inputting your notes.
The bottom text area will display the summarized output.


Enter or paste your notes into the top text area.
Click the "Submit" button to start the summarization process.
The status label will update you on the progress of the summarization.
Once complete, the summary will appear in the bottom text area.
To start a new summarization task, click the "Clear" button to reset both text areas.

Troubleshooting

If you encounter any issues, check the console output for error messages. The application logs detailed information which can help in debugging.
Ensure that your API key is correctly set and that you have sufficient credits in your OpenAI account.
Verify that your custom assistant is properly configured with the text summarization skill.

Contributing
Contributions to the AI-Powered Note Summarizer are welcome. Please feel free to submit a Pull Request.
License
This project is open source and available under the MIT License.
Acknowledgements

This project uses the OpenAI API. Thanks to OpenAI for providing this powerful tool.
Built with Python and Tkinter.

Contact
If you have any questions or feedback, please open an issue in this repository.
