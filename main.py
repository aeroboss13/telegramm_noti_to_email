import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, recipient, sender, password):
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipient

    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(sender, password)
    smtp_server.send_message(message)
    smtp_server.quit()

def handle_telegram_message(message):
    subject = 'New Telegram Message Received'
    body = f'Message content: {message["text"]}'
    recipient = 'you@example.com'
    sender = 'sender@example.com'
    password = 'your_email_password'
    send_email(subject, body, recipient, sender, password)

# assume that the message is a dictionary containing the message text
message = {'text': 'Hello, World!'}
handle_telegram_message(message)
