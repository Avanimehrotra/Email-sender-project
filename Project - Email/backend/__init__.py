# backend/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register the blueprint here, avoiding circular import
    from backend.routes.email_routes import email_routes
    app.register_blueprint(email_routes)
    app = Flask(__name__, template_folder="../frontend/templates")

    return app
