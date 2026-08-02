import smtplib
from email.message import EmailMessage
from getpass import getpass

def send_email(sender_email, app_password, receiver_email, subject, body):

    try:
        message = EmailMessage()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(message)

        print("\nEmail sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("\nAuthentication failed!")
        print("Check your Gmail address and App Password.")

    except smtplib.SMTPRecipientsRefused:
        print("\nRecipient email address is invalid.")

    except smtplib.SMTPConnectError:
        print("\nUnable to connect to Gmail SMTP server.")

    except Exception as error:
        print(f"\nFailed to send email.\nReason: {error}")


print("=" * 50)
print("           EMAIL AUTOMATION")
print("=" * 50)

# Sender Email
while True:
    sender = input("Sender Gmail: ").strip()

    if "@" in sender and "." in sender:
        break

    print("Invalid email address. Please try again.")

# App Password (Hidden)
password = getpass("App Password: ")

# Receiver Email
while True:
    receiver = input("Receiver Email: ").strip()

    if "@" in receiver and "." in receiver:
        break

    print("Invalid email address. Please try again.")

# Subject
subject = input("Subject: ").strip()

# Message
print("\nEnter your message.")
print("Press ENTER twice to finish.\n")

lines = []

while True:
    line = input()

    if line == "":
        break

    lines.append(line)

body = "\n".join(lines)

if not body.strip():
    print("\nNo message entered.")
else:
    send_email(
        sender,
        password,
        receiver,
        subject,
        body
    )