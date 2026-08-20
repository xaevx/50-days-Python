# AI Chatbot

A command-line **AI Chatbot** built with Python and the Groq API.

The chatbot communicates with a Large Language Model through Groq's API and maintains conversation history during the current session.

## Features

* AI-powered conversations
* Fast responses using Groq
* Multi-turn conversations
* Session-based conversation memory
* API key stored as an environment variable
* Command-line interface
* Exit command

## Requirements

Install the Groq Python SDK:

```bash
python -m pip install groq
```

## API Key Setup

Create a Groq API key and store it as an environment variable.

### Windows PowerShell

```powershell
$env:GROQ_API_KEY="your_api_key_here"
```

Then run:

```powershell
python AI_Chatbot.py
```

For Model choose active model

```models
Any appropriate model from groq.com/models
```

> Never upload your API key to GitHub.

## Run the Project

```bash
python AI_Chatbot.py
```

Example:

```text
==================================================
              AI CHATBOT
==================================================
Type 'exit' to quit.

You: What is Python?

AI: Python is a high-level programming language...
```

Type:

```text
exit
```

to close the chatbot.

## How It Works

```text
User Input
    ↓
Python
    ↓
Conversation History
    ↓
Groq API
    ↓
Large Language Model
    ↓
Generated Response
    ↓
Python
    ↓
Terminal
```

## Conversation Memory

The chatbot stores messages in a Python list:

```python
conversation = [
    {
        "role": "system",
        "content": "You are a helpful and friendly AI assistant."
    }
]
```

User messages are stored as:

```python
{
    "role": "user",
    "content": user_input
}
```

AI responses are stored as:

```python
{
    "role": "assistant",
    "content": assistant_reply
}
```

The complete conversation is sent to the model with each request.

This allows the AI to use previous messages as context.

## API Security

The API key is loaded using:

```python
os.environ.get("GROQ_API_KEY")
```

This prevents the secret key from being directly written into the source code.

Never commit API keys to GitHub.

## Modules Used

* Python 3
* Groq API
* Groq Python SDK
* Large Language Models

## What i learned

* API Integration
* Large Language Models
* Natural Language Processing
* Environment Variables
* JSON-like Message Structures
* Conversation History
* Exception Handling
* Functions
* Loops
* User Input

> **Note:** This project requires an active Groq API key and an internet connection.

---

⭐ Part of my **#50DaysOfPython** challenge.
