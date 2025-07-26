from flask import render_template, request, redirect, url_for, jsonify, abort
from models.todo import Todo
from extensions.database import db


def index():
    todos = db.session.execute(
        db.select(Todo)
        .order_by(Todo.added_on.desc())
    ).scalars().all()
    return render_template('main/index.html', todos=todos)


def create():
    return render_template('main/create.html')


def store():
    text = request.form.get('text')

    todo = Todo(text=text)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('main.index'))


def edit(todo_id: int):
    todo = db.get_or_404(Todo, todo_id)

    return render_template('main/edit.html', todo=todo)


def update(todo_id: int):
    todo = db.get_or_404(Todo, todo_id)

    if not request.json:
        return jsonify({'success': False}), 400

    for field, value in request.json.items():
        if field in Todo.allowed_fields and hasattr(todo, field):
            setattr(todo, field, value)
        else:
            # Optionally: skip or return 400 if the field doesn't exist
            abort(400, description=f"Unknown field: {field}")

    db.session.commit()

    return jsonify({'success': True})


def destroy(todo_id: int):
    todo = db.get_or_404(Todo, todo_id)

    db.session.delete(todo)
    db.session.commit()

    return jsonify({'success': True})
