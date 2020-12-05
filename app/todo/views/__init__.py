from flask import Blueprint

bp = Blueprint('todo', __name__, url_prefix='/')

from . import calendar, team, projects, dashboard