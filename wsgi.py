import os
import app
from dotenv import load_dotenv
from flask import Flask

load_dotenv()


def create_app():
    flask_config = os.getenv('FLASK_CONFIG', 'production')
    app_instance = app.create_app(config_name=flask_config)
    return app_instance
