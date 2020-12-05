from flask_login import login_required
from flask import render_template

from . import bp




@bp.route('/calendar')
@login_required
def calendar():
  calendar = True
  context = {
    'calendar': calendar,
  }
  return render_template('todo/calendar.html', context=context)