# backend/routes/analytics.py
from flask import Blueprint, jsonify
from database.schemas import get_status_counts

analytics = Blueprint("analytics", __name__)

@analytics.route("/api/analytics", methods=["GET"])
def get_analytics():
    status_counts = get_status_counts()  # Fetch the status counts
    return jsonify(status_counts)
