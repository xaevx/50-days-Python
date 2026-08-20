import os
from groq import Groq

API_KEY = os.environ.get("GROQ_API_KEY") 

if not API_KEY:

    print("Groq API key not found.")
    print("Please set the GROQ_API_KEY environment variable.")
    exit()

client = Groq(
    api_key=API_KEY
)

MODEL = "Enter_your_appropriate_model" # from groq.com/models

conversation = [
    {
        "role": "system",
        "content": "You are a helpful and friendly AI assistant."
    }
]

print("=" * 50)
print("              AI CHATBOT")
print("=" * 50)
print("Type 'exit' to quit.")
print()

while True:

    user_input = input("You: ").strip()

    if not user_input:

        print("Please enter a message.")
        continue

    if user_input.lower() == "exit":

        print("Goodbye!")
        break

    conversation.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    try:

        response = client.chat.completions.create(
            model=MODEL,
            messages=conversation
        )

        assistant_reply = response.choices[0].message.content

        conversation.append(
            {
                "role": "assistant",
                "content": assistant_reply
            }
        )

        print("\nAI:", assistant_reply)
        print()

    except Exception as error:

        print("\nError:", error)
        print("Please check your API key and internet connection.\n")