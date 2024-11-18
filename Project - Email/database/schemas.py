# database/schemas.py
from pymongo import MongoClient
from datetime import datetime

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client.email_sender_db
email_status_collection = db.email_statuses

def log_email_status(email, status, batch_id=None):
    """Log the initial status of an email."""
    email_status_collection.insert_one({
        "recipient_email": email,
        "status": status,
        "batch_id": batch_id,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    })

def update_email_status(email, status, batch_id=None):
    """Update the status of an email."""
    email_status_collection.update_one(
        {"recipient_email": email, "batch_id": batch_id},
        {"$set": {"status": status, "updated_at": datetime.now()}},
        upsert=True
    )

def get_status_counts():
    """Retrieve counts of each email status."""
    pipeline = [
        {"$group": {"_id": "$status", "count": {"$sum": 1}}}
    ]
    # Return a dictionary with status as key and count as value
    return {item["_id"]: item["count"] for item in email_status_collection.aggregate(pipeline)}
