from flask import Blueprint
from app.blueprints.main import controllers as main

blueprint = Blueprint('main', __name__, template_folder='templates')

blueprint.get('/')(main.index)
blueprint.get('/create')(main.create)
blueprint.post('/')(main.store)
blueprint.get('/<int:todo_id>/edit')(main.edit)
blueprint.put('/<int:todo_id>')(main.update)
blueprint.delete('/<int:todo_id>')(main.destroy)
