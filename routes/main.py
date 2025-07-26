from flask import Blueprint
from controllers import main

main_route = Blueprint('main', __name__)


main_route.get('/')(main.index)
main_route.get('/create')(main.create)
main_route.post('/')(main.store)
main_route.get('/<int:todo_id>/edit')(main.edit)
main_route.put('/<int:todo_id>')(main.update)
main_route.delete('/<int:todo_id>')(main.destroy)
