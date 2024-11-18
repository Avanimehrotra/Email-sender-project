from flask import Flask, request, jsonify
from backend.routes.email_routes import email_routes
from flask import render_template

app = Flask(__name__, template_folder="../frontend")  # Adjust template folder if needed
app.register_blueprint(email_routes, url_prefix='/api')  # Use email_routes, not email_bp

@app.route('/api/schedule_email', methods=['POST'])
def schedule_email():
    # Your code for scheduling the email
    return jsonify({'message': 'Email scheduled successfully!'}), 200
    print("Received POST request to schedule email.")  # Log request

    data = request.get_json()
    print(f"Received data: {data}")  # Log request data (useful for debugging payload issues)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask application
