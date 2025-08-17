from flask import Flask
from . import cloud_demo
from . import proxy
from . import database
from . import method_override
from . import flash_form

# List of extensions to load
extensions_list = [
    proxy,
    database,
    method_override,
    flash_form,
]


def init_app(app: Flask):
    '''
    Initialize all the extensions needed by the app.
    '''

    # For Google App Engine and Render deployment
    # Use an ephemeral database for temporary storage
    cloud_demo.deploy_database()

    # Load each extension in succession
    for extension in extensions_list:
        extension.init_app(app)


def init_migration(app: Flask):
    '''
    Initialize Flask-Migrate for database migrations
    '''

    database.migrate(app)
