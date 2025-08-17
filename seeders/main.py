import click
from flask import Flask, Blueprint
from app.extensions.database import db
from app.models.todo import Todo
from faker import Faker
from . import seeder_blueprint


@seeder_blueprint.cli.command('todos')
def todos() -> None:
    fake = Faker()
    for _ in range(100):
        random_text = fake.sentence(100)
        todo = Todo(text=random_text, is_done=False)
        db.session.add(todo)
    db.session.commit()
    print('100 todos has been added.')


@seeder_blueprint.cli.command('clean')
def clean() -> None:
    db.session.execute(db.delete(Todo))
    db.session.commit()
    print('The database has been cleaned!')
