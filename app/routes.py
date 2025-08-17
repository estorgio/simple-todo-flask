from flask import Flask
from app.blueprints.main import routes as main_route


def init_app(app: Flask) -> None:

    # Main routes
    app.register_blueprint(main_route.blueprint, url_prefix='/')
