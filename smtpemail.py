import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port=25):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Send the email without authentication
        server.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == "__main__":
    # Set your email and server details
    sender_email = 'dineshatit@gmail.com'
    receiver_email = 'dineshatit@gmail.com'
    subject = 'Test Email without Authentication'
    body = 'This is a test email without authentication.'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Default port for unsecured SMTP

    # Send the email
    send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port)
