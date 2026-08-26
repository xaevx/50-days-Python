import os
import datetime
import webbrowser
import speech_recognition as sr
import pyttsx3
from groq import Groq

MODEL = "openai/gpt-oss-20b"

API_KEY = os.environ.get("GROQ_API_KEY")

if not API_KEY:

    print("Groq API key not found.")
    print("Please set the GROQ_API_KEY environment variable.") 
    exit()

client = Groq(api_key=API_KEY)

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 175)

conversation = [
    {
        "role": "system",
        "content": (
            "You are a helpful personal AI assistant. "
            "Give clear, concise and friendly answers."
        )
    }
]

def speak(text):

    print(f"\nAssistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:

            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

            print("Recognizing...")

            command = recognizer.recognize_google(audio)

            print(f"You: {command}")
            return command.lower()

        except sr.WaitTimeoutError:

            print("No speech detected.")
            return ""

        except sr.UnknownValueError:

            print("I could not understand that.")
            return ""

        except sr.RequestError:

            print("Speech recognition service is unavailable.")
            return ""

def ask_ai(user_input):

    conversation.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    try:

        response = client.chat.completions.create(
            model=MODEL,
            messages=conversation,
            temperature=0.7,
            max_tokens=500
        )

        reply = response.choices[0].message.content

        conversation.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

        return reply

    except Exception as error:

        print(f"\nAI Error: {error}")
        return "Sorry, I could not connect to the AI service."

def process_command(command):

    if not command:
        return True

    if (
        "hello" in command
        or "hi" in command
        or "hey" in command
    ):

        speak("Hello! How can I help you?")
        return True

    if "time" in command:

        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
        return True

    if "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {current_date}.")
        return True

    if "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
        return True

    if "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
        return True

    if "open github" in command:
        speak("Opening GitHub.")
        webbrowser.open("https://github.com")

        return True

    if (
        "exit" in command
        or "quit" in command
        or "goodbye" in command
        or "stop assistant" in command
    ):

        speak("Goodbye! See you later.")
        return False

    response = ask_ai(command)
    speak(response)
    return True

print("=" * 55)
print("             PERSONAL AI ASSISTANT")
print("=" * 55)

print("Voice assistant is ready.")
print("Say 'exit' or 'quit' to close the assistant.")

speak("Personal AI assistant started. How can I help you?")

running = True

while running:
    command = listen()
    running = process_command(command)