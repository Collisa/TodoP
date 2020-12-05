from flask_login import login_required
from flask import render_template

from . import bp



@bp.route('/projects')
@login_required
def projects():
  projects = True
  context = {
    'projects': projects,
  }
  return render_template('todo/projects.html', context=context)