from celery import Celery
from datetime import datetime, timedelta
import requests
import os

SENDINBLUE_API_KEY = os.getenv("SENDINBLUE_API_KEY")

celery = Celery('email_tasks', broker='redis://localhost:6379/0')

@celery.task
def send_email_task(recipient, subject, body):
    """Send email using Sendinblue API."""
    url = "https://api.sendinblue.com/v3/smtp/email"
    headers = {
        "Content-Type": "application/json",
        "api-key": SENDINBLUE_API_KEY
    }
    payload = {
        "sender": {"email": "your_email@domain.com"},
        "to": [{"email": recipient}],
        "subject": subject,
        "htmlContent": body
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Email sent to {recipient}: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {e}")

from datetime import datetime

def schedule_email(recipient, subject, body, send_time):
    """Schedule email to be sent at a specific time."""
    countdown = (send_time - datetime.now()).total_seconds()
    send_email_task.apply_async((recipient, subject, body), countdown=countdown)
