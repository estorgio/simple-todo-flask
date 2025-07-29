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
    todo = Todo()
    todo.fill(request.form)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('main.index'))


def edit(todo_id: int):
    todo = db.get_or_404(Todo, todo_id)

    return render_template('main/edit.html', todo=todo)


def update(todo_id: int):
    todo = db.get_or_404(Todo, todo_id)

    if request.is_json and request.json:
        todo.fill(request.json)
        db.session.commit()
        return jsonify({'success': True})
    else:
        todo.fill(request.form)
        db.session.commit()
        return redirect(url_for('main.index'))


def destroy(todo_id: int):
    todo = db.get_or_404(Todo, todo_id)

    db.session.delete(todo)
    db.session.commit()

    if request.is_json and request.json:
        return jsonify({'success': True})
    else:
        return redirect(url_for('main.index'))
