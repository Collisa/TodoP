from flask_login import login_required
from flask import render_template

from . import bp


@bp.route('/team')
@login_required
def team():
  team = True
  context = {
    'team': team,
  }
  return render_template('todo/team.html', context=context)