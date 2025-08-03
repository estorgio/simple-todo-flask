import click
from flask import Flask, Blueprint
from extensions.database import db
from models.todo import Todo
from faker import Faker

blueprint = Blueprint('seeders', __name__)


@blueprint.cli.command('todos')
def todos():
    fake = Faker()
    for _ in range(100):
        random_text = fake.sentence(100)
        todo = Todo(text=random_text, is_done=False)
        db.session.add(todo)
    db.session.commit()
    print('100 todos has been added.')


@blueprint.cli.command('clean')
def clean():
    db.session.execute(db.delete(Todo))
    db.session.commit()
    print('The database has been cleaned!')


def init_app(app: Flask) -> None:
    app.register_blueprint(blueprint)
