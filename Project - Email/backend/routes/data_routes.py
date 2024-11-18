# backend/routes/data_routes.py
import pandas as pd
from flask import Blueprint, jsonify, request

data_routes = Blueprint('data_routes', __name__)

@data_routes.route('/api/fetch_google_sheet_csv', methods=['POST'])
def fetch_google_sheet_csv():
    print("Received request at /api/fetch_google_sheet_csv")  # Debug log
    csv_url = request.json.get("csv_url")
    print(f"CSV URL received: {csv_url}")
    try:
        #csv_url = request.json.get("csv_url")
        data = pd.read_csv(csv_url)
        columns = data.columns.tolist()
        records = data.to_dict(orient='records')
        print("Data fetched successfully")
        return jsonify({'columns': columns, 'data': records})
    except Exception as e:
        print(f"Error fetching CSV data: {e}")
        return jsonify({'error': str(e)}), 400
