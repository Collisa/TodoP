from flask import Blueprint, request, render_template, redirect, url_for
from .models import Todo

from flask_login import login_required

bp = Blueprint('todo', __name__, url_prefix='/')

@bp.route('')
@login_required
def index():

  todos = Todo.query.all()

  dashboard = True

  context = {
    'dashboard': dashboard,
    'todos': todos
  }

  return render_template('todo/index.html', context=context)




@bp.route('/create', methods=['POST'])
@login_required
def create():
  # title = request.form['title']
  body = request.form['body']
  error = None

  if not body:
    error = 'Body is required.'

  if error is not None:
    flash(error)
  else:
    db = get_db()
    db.execute(
      'INSERT INTO todos (title, body, creator_id)'
      ' VALUES (?, ?, ?)',
      (None, body, g.user['id'])
    )
    db.commit()
    return redirect(url_for('index'))




def get_todo(id, check_creator=True):
    todo = get_db().execute(
        'SELECT p.id, title, body, created, creator_id, username'
        ' FROM todos p JOIN user u ON p.creator_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if todo is None:
        abort(404, "Todo id {0} doesn't exist.".format(id))

    if check_creator and todo['creator_id'] != g.user['id']:
        abort(403)

    return todo




@bp.route('/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
    
  db = get_db()

  todos = db.execute(
    'SELECT p.id, title, body, created, creator_id, username'
    ' FROM todos p JOIN user u ON p.creator_id = u.id'
    ' ORDER BY created ASC'
  ).fetchall()

  dashboard = True

  context = {
    'dashboard': dashboard,
    'todos': todos
  }

  edit_todo = get_todo(id)

  edit = True

  if request.method == 'POST':
      # title = request.form['title']
      body = request.form['body']
      error = None

      if not body:
          error = 'Body is required.'

      if error is not None:
          flash(error)
      else:
          
          db.execute(
              'UPDATE todos SET title = ?, body = ?'
              ' WHERE id = ?',
              (None, body, id)
          )
          db.commit()
          return redirect(url_for('index'))

  return render_template('todo/index.html', edit_todo=edit_todo, edit=edit, context=context)




@bp.route('/team')
@login_required
def team():
  team = True
  context = {
    'team': team,
  }
  return render_template('todo/team.html', context=context)

@bp.route('/projects')
@login_required
def projects():
  projects = True
  context = {
    'projects': projects,
  }
  return render_template('todo/projects.html', context=context)

@bp.route('/calendar')
@login_required
def calendar():
  calendar = True
  context = {
    'calendar': calendar,
  }
  return render_template('todo/calendar.html', context=context)