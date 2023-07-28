import os
from dotenv import load_dotenv
from emailer import send_bulk_emails

load_dotenv(override=True)


if __name__ == "__main__":
    send_bulk_emails(
        ["test1@gmail.com", "test2@gmail.com"],
        "Test Title",
        "Test Body",
        os.environ.get("SENDER_EMAIL_ADDRESS"),
        os.environ.get("SENDER_PASSWORD"),
    )
