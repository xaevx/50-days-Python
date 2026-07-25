questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Chennai", "B. New Delhi", "C. Mumbai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language is primarily used for AI and Data Science?",
        "options": ["A. Java", "B. C++", "C. Python", "D. PHP"],
        "answer": "C"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Elon Musk"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    }
]


score = 0

print("=" * 45)
print("         QUIZ APPLICATION")
print("=" * 45)

for index, question in enumerate(questions, start=1):

    print(f"\nQuestion {index}")
    print(question["question"])

    for option in question["options"]:
        print(option)

    answer = input("\nEnter Your Answer (A/B/C/D): ").upper()

    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct Answer: {question['answer']}")

print("\n" + "=" * 45)
print("           QUIZ COMPLETED")
print("=" * 45)

print(f"Score : {score}/{len(questions)}")

percentage = (score / len(questions)) * 100

print(f"Percentage : {percentage:.2f}%")

if percentage >= 80:
    print("Excellent!")
elif percentage >= 60:
    print("Good Job!")
elif percentage >= 40:
    print("Keep Practicing!")
else:
    print("Better Luck Next Time!")