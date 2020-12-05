from app.todo.forms import TodoForm
from flask import request, render_template, redirect, url_for
from flask_login import login_required, current_user

from . import bp
from app.todo.models import Todo
from app import db
from app.todo.decorators import get_todo



@bp.route('')
@login_required
def index():

  todos = Todo.query.all()

  dashboard = True

  context = {
    'dashboard': dashboard,
    'todos': todos,
  }

  return render_template('todo/index.html', context=context, form=TodoForm())

@bp.route('/done')
@login_required
def show_finished():

  todos = Todo.query.filter_by(done=True).all()

  dashboard = True

  context = {
    'dashboard': dashboard,
    'todos': todos,
  }

  return render_template('todo/index.html', context=context, form=TodoForm())

@bp.route('/todo')
@login_required
def show_undone():

  todos = Todo.query.filter_by(done=False).all()

  dashboard = True

  context = {
    'dashboard': dashboard,
    'todos': todos,
  }

  return render_template('todo/index.html', context=context, form=TodoForm())




@bp.route('/create', methods=['POST'])
@login_required
def create():
  form = TodoForm(request.form)

  if request.method == 'POST':
    todo = Todo(
      body=form.body.data,
      priority=form.priority.data,
      tags=form.tags.data,
      user_id=current_user.id
    )

    db.session.add(todo)
    db.session.commit()
  
  return redirect(url_for('todo.index'))



@bp.route('/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
    
  todos = Todo.query.all()

  dashboard = True
  edit = True

  context = {
    'dashboard': dashboard,
    'todos': todos,
    'edit': edit,
  }
  edit_todo = get_todo(id)

  edit_form = TodoForm()
  if request.method == 'POST':
  
    edit_todo.body=edit_form.body.data
    edit_todo.priority=edit_form.priority.data
    edit_todo.tags=edit_form.tags.data
    edit_todo.user_id=current_user.id
    
    
    db.session.commit()
    return redirect(url_for('todo.index'))
  return render_template('todo/index.html', edit_todo=edit_todo, context=context, edit_form=TodoForm(obj=edit_todo), form=TodoForm())



@bp.route('/check_off/<int:id>')
@login_required
def check_off(id):

  todo = get_todo(id)
    
  todo.done = True
  db.session.commit()
  return redirect(url_for('todo.index'))


