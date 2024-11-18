# backend/routes/email_routes.py
import ssl
import requests
from flask import Blueprint, jsonify, request
from datetime import datetime
from backend.tasks.email_tasks import schedule_email

email_routes = Blueprint('email_routes', __name__)

@email_routes.route("/api/schedule_email", methods=["POST"])
def schedule_email_route():
    data = request.json
    recipient = data.get("recipient")
    subject = data.get("subject")
    body = data.get("body")
    send_time_str = data.get("send_time")

    try:
        # Parse send_time from string to datetime
        send_time = datetime.strptime(send_time_str, "%Y-%m-%d %H:%M:%S")
        schedule_email(recipient, subject, body, send_time)
        return jsonify({"message": "Email scheduled successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@email_routes.route('/test', methods=['GET'])
def test_route():
    return jsonify({"message": "Test route works!"})

# Email sending function
def send_email(sender, recipient, subject, html_content):
    url = 'https://api.sendinblue.com/v3/smtp/email'
    headers = {
        'api-key': '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',  # Replace with your Sendinblue API key
        'Content-Type': 'application/json'
    }
    data = {
        'sender': {'email': sender},
        'to': [{'email': recipient}],
        'subject': subject,
        'htmlContent': html_content
    }

    try:
        response = requests.post(url, headers=headers, json=data, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Set the sender email here
SENDER_EMAIL = "avanimehrotra2004@gmail.com"

@email_routes.route('/send_email', methods=['POST'])
def send_email_route():
    # Log incoming request for debugging
    print(f"Request data: {request.json}")

    # Extract the recipient, subject, and HTML content from the request
    recipient = request.json.get('recipient')
    subject = request.json.get('subject')
    html_content = request.json.get('body')  # Change 'htmlContent' to 'body'

    # Validate fields
    if not recipient or not subject or not html_content:
        return jsonify({"error": "Missing required fields"}), 400

    # Call the send_email function with the sender fixed to the specified email
    result = send_email(SENDER_EMAIL, recipient, subject, html_content)
    return jsonify(result)
