import smtplib
import threading
from email.message import EmailMessage


def send_email(
    email_address,
    email_title,
    email_body,
    sender_email,
    sender_password,
    smtp_server="smtp.gmail.com",
    smtp_port=587,
):
    try:
        msg = EmailMessage()
        msg["From"] = sender_email
        msg["To"] = email_address
        msg["Subject"] = email_title
        msg.set_content(email_body)

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        server.login(sender_email, sender_password)

        server.send_message(msg)

        server.quit()

        print(f"[SUCCESS] {email_address}")
    except Exception:
        print(f"[FAILURE] {email_address}")


def send_bulk_emails(
    email_list, email_title, email_body, sender_email, sender_password
):
    threads = []

    for recipient in email_list:
        thread = threading.Thread(
            target=send_email,
            args=(recipient, email_title, email_body, sender_email, sender_password),
        )
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
