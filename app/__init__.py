from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    

from .todo.models import Todo
from .auth.models import User

@app.errorhandler(404)
def not_found(error):
  return render_template('404.html'), 404


from app.auth.views import bp as authModule
from app.todo.views import bp as todoModule
app.register_blueprint(authModule)
app.register_blueprint(todoModule)



# Later on you'll import the other blueprints the same way:
#from app.comments.views import mod as commentsModule
#from app.posts.views import mod as postsModule
#app.register_blueprint(commentsModule)
#app.register_blueprint(postsModule)