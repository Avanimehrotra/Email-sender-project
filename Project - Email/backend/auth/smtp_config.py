# backend/auth/smtp_config.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_smtp(provider, sender_email, password, recipient_email, subject, body):
    smtp_servers = {
        "gmail": {"server": "smtp.gmail.com", "port": 587},
        "outlook": {"server": "smtp.office365.com", "port": 587},
        "sendgrid": {"server": "smtp.sendgrid.net", "port": 587},
        "mailgun": {"server": "smtp.mailgun.org", "port": 587},
        "ses": {"server": "email-smtp.us-east-1.amazonaws.com", "port": 587},
    }

    if provider not in smtp_servers:
        raise ValueError(f"Unsupported email provider: {provider}")

    smtp_info = smtp_servers[provider]
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_info["server"], smtp_info["port"]) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
