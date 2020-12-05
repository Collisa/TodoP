from flask_login import current_user
from .models import Todo

def get_todo(id, check_creator=True):
    todo = Todo.query.filter_by(id=id).first()

    if todo is None:
        abort(404, f"Todo id {id} doesn't exist.")

    if check_creator and todo.user_id != current_user.id:
        abort(403)

    return todo