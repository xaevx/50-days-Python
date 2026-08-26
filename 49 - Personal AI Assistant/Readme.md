# Personal AI Assistant

A **Personal AI Assistant** built with Python that combines artificial intelligence, voice recognition, text-to-speech, web automation, and basic system commands into a single application.

The project uses **Groq** to provide AI-powered responses, **SpeechRecognition** for voice input, and **pyttsx3** for text-to-speech.

## Features

- AI-powered conversations
- Voice input
- Speech recognition
- Text-to-speech responses
- Conversation memory
- Current time
- Current date
- Open Google
- Open YouTube
- Open GitHub
- Natural language interaction
- Error handling
- Environment variable API key
- Voice-controlled exit

## Requirements

Install the required packages:

```bash
python -m pip install groq SpeechRecognition pyttsx3 PyAudio
```

If PyAudio installation fails on Windows:

```bash
python -m pip install pipwin
pipwin install pyaudio
```

## API Key

This project uses the **Groq API** to generate AI responses.

The API key should be stored as an environment variable.

### Windows PowerShell

```powershell
$env:GROQ_API_KEY="YOUR_GROQ_API_KEY"
```

Verify that Python can access the key:

```powershell
python -c "import os; print(bool(os.getenv('GROQ_API_KEY')))"
```

Expected output:

```text
True
```

## Security

Never place your API key directly inside the Python source code.

Do not use:

```python
API_KEY = "YOUR_API_KEY"
```

## Run the Project

Run:

```bash
python Personal_AI_Assistant.py
```

The assistant will initialize and begin listening through the microphone.

## AI Model

The project uses a Groq-hosted language model:

```text
openai/gpt-oss-20b #You can use any models from Groq
```

## Modules Used

- Python 3
- Groq
- SpeechRecognition
- PyAudio
- pyttsx3
- datetime
- webbrowser
- os

## What i learned

- AI API integration
- Large Language Models
- Voice assistants
- Speech recognition
- Text-to-speech
- Conversation memory
- API authentication
- Environment variables
- Python automation
- Web browser automation
- Exception handling
- Asynchronous-style event workflows
- Combining multiple Python libraries
- Building a multi-feature application

---

⭐ Part of my **#50DaysOfPython** challenge.