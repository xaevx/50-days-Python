# Voice Assistant

A simple **Voice Assistant** built with Python that listens to spoken commands, converts speech into text, processes the command, and responds using text-to-speech.

The project combines **Speech Recognition**, **Text-to-Speech**, and basic Python automation.

## Features

- Voice input through microphone
- Speech-to-text conversion
- Text-to-speech responses
- Tell the current time
- Tell the current date
- Open Google
- Open YouTube
- Open GitHub
- Basic conversation commands
- Voice-controlled exit
- Error handling

## Requirements

Install the required packages:

```bash
python -m pip install SpeechRecognition pyttsx3 PyAudio
```

If PyAudio installation fails on Windows:

```bash
python -m pip install pipwin
pipwin install pyaudio
```

## Run the Project

```bash
python Voice_Assistant.py
```

The assistant will start listening through your microphone.

## Example

```text
==================================================
              VOICE ASSISTANT
==================================================

Assistant: Voice assistant started. How can I help you?

Listening...
Recognizing...

You: What is the time?

Assistant: The current time is 10:35 PM
```

## Available Commands (Only these commands work /cuz i wanted it to be lightweight)

```text
Hello
Hi
What is the time?
What is today's date?
Open Google
Open YouTube
Open GitHub
Stop
Exit
Quit
```

## How It Works

```text
Microphone (Make sure the Microphone is connected)
     ↓
Speech Recognition
     ↓
Convert Speech to Text
     ↓
Process Command
     ↓
Perform Action
     ↓
Generate Response
     ↓
Text-to-Speech
     ↓
Speaker
```

## Speech Recognition

The program uses:

```python
speech_recognition
```

to capture audio from the microphone and convert spoken words into text.

The main recognition function is:

```python
recognizer.recognize_google(audio)
```

The recognized speech is then converted to lowercase so that commands can be compared more easily.

## Text-to-Speech

The project uses:

```python
pyttsx3
```

to convert text into spoken audio.

The assistant uses:

```python
engine.say(text)
engine.runAndWait()
```

to speak its responses.

## Modules Used

- Python 3
- SpeechRecognition
- PyAudio
- pyttsx3
- datetime
- webbrowser

## What i learned

- Speech Recognition
- Voice Input
- Text-to-Speech
- Microphone Handling
- Audio Processing
- Python Automation
- Functions
- Conditional Statements
- Exception Handling
- Web Browser Automation
- Working with External Libraries

---

⭐ Part of my **#50DaysOfPython** challenge.