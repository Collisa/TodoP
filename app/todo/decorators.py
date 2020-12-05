from app import todo

from .models import Todo
from app import db

def get_todo(id):
    todo = Todo.query.filter_by(id=id).first()
    return todo
    