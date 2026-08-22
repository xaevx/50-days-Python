import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):

    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            print("Recognizing...")
            command = recognizer.recognize_google(audio)

            print("You:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""

        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return ""

        except sr.RequestError:
            print("Speech recognition service is unavailable.")
            return ""

def process_command(command):

    if "hello" in command or "hi" in command:

        speak("Hello! How can I help you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")

    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "open github" in command:
        speak("Opening GitHub.")
        webbrowser.open("https://github.com")

    elif "stop" in command or "exit" in command or "quit" in command:
        speak("Goodbye!")
        return False

    else:
        speak("I don't know that command yet.")

    return True

print("=" * 50)
print("              VOICE ASSISTANT")
print("=" * 50)

speak(
    "Voice assistant started. How can I help you?"
)

running = True

while running:
    command = listen()

    if command:
        running = process_command(
            command
        )