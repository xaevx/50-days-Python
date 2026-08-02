# Email Automation

A simple command-line **Email Automation** application built with Python. It securely sends emails using Gmail's SMTP server and a Google App Password.

## Features

- Send Emails Automatically
- Secure Login with Google App Password
- Custom Subject & Multi-line Message
- Sender & Receiver Email Validation
- Hidden Password Input
- Fast & Lightweight Command-Line Interface
- Robust Error Handling

## Requirements

Python comes with all the required libraries.

No external packages are needed.

## Run the Project

```bash
python Email_Automation.py
```

## Example

```
==================================================
               EMAIL AUTOMATION
==================================================

Sender Gmail:
example@gmail.com

App Password:
****************(Password won't be visible, Generated from https://myaccount.google.com/apppasswords)

Receiver Email:
friend@gmail.com

Subject:
Python Test

Enter your message.
Press ENTER twice to finish.

Hello,
This is a test email sent using Python.

Email sent successfully!
```

## Modules Used

- Python 3
- smtplib
- email.message
- getpass

## What i learned

- SMTP Protocol
- Secure Email Authentication
- Functions
- Exception Handling
- User Input Validation
- Multi-line Input Handling
- Python Standard Library
* Email Automation

## ⚠️ Important

Gmail **does not allow your regular account password** for SMTP authentication.

Use a **Google App Password** of https://myaccount.google.com/apppasswords instead:

1. Enable **2-Step Verification** on your Google Account.
2. Generate a **Google App Password** or.
3. Use the generated App Password when prompted by the program.

> 🔒 Never share your App Password or hardcode it into your source code.

---

⭐ Part of my **#50DaysOfPython** challenge.
