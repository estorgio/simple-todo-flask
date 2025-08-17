from flask import Flask
from config import config_options
from . import extensions
from . import routes


def create_app(config_name='production') -> Flask:
    '''
    Create a new Flask instance of the web app
    '''

    app = Flask(__name__,
                static_folder='static',
                static_url_path='/'
                )
    app.config.from_object(config_options[config_name])

    # Load extensions
    extensions.init_app(app)

    # Load routes here
    routes.init_app(app)

    # Initialize database migration
    extensions.init_migration(app)

    # Load database seeders
    load_seeders(app)

    return app


def load_seeders(app: Flask) -> None:
    import seeders
    seeders.init_app(app)
