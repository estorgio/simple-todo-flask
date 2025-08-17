import importlib
import pkgutil
from types import ModuleType
from flask import Flask, Blueprint

seeder_blueprint = Blueprint('seeders', __name__)


def init_app(app: Flask) -> None:

    # Load all seeders
    load_all_seeders()

    app.register_blueprint(seeder_blueprint)


def load_all_seeders() -> list[ModuleType]:
    modules = []
    for _, module_name, _ in pkgutil.iter_modules(__path__):
        loaded_module = importlib.import_module(f"{__name__}.{module_name}")
        modules.append(loaded_module)
    return modules
