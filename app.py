#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()


def create_app() -> Flask:
    # For Google App Engine and Render - deploy sqlite db to /tmp
    from extensions import cloud_demo
    cloud_demo.deploy_database()

    app = Flask(__name__,
                template_folder='views',
                static_folder='public',
                static_url_path='/'
                )
    app.secret_key = os.getenv('SECRET_KEY')

    from extensions import database
    database.init_app(app)

    from extensions import method_override
    method_override.init_app(app)

    from extensions import flash_form
    flash_form.init_app(app)

    from seeders import seeder
    seeder.init_app(app)

    from routes.main import main_route
    app.register_blueprint(main_route, url_prefix='/')

    database.migrate(app)

    return app
