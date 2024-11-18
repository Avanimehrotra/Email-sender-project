# backend/routes/webhook_routes.py
from flask import Blueprint, request, jsonify
from database.schemas import update_email_status  # Assume this updates email status in the database

webhook_routes = Blueprint("webhook_routes", __name__)

@webhook_routes.route('/webhook/email_status', methods=['POST'])
def email_status_webhook():
    data = request.json
    for event in data:
        email = event.get("email")
        event_type = event.get("event")  # e.g., "delivered", "bounce", "open"
        
        # Update database status based on event type
        if event_type == "delivered":
            update_email_status(email, "delivered")
        elif event_type == "bounce":
            update_email_status(email, "bounced")
        elif event_type == "open":
            update_email_status(email, "opened")

    return jsonify({"message": "Status updated successfully"}), 200
