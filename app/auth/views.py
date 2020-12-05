from sqlalchemy.exc import IntegrityError
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user

from app import db
from app.auth.forms import RegisterForm, LoginForm
from app.auth.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')




@bp.before_request
def before_request():
  # Pull user's profile from the database before every request is treated.
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id'])




@bp.route('login/', methods=['GET','POST'])
def login():
  form = LoginForm(request.form)

  # make sure data is validated, but doesn't validate password is right
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()

    # we use werkzeug to validate user's passowrd
    if user and check_password_hash(user.password, form.password.data):
      # the session can't be modified as it's signed, 
      # it's a safe place to store the user id
      login_user(user)
      flash(f'Welcome {user.name}')
      return redirect(url_for('todo.index'))
    
    flash('Wrong email or password.')
  return render_template('auth/login.html', form=form)




@bp.route('register/', methods=['GET','POST'])
def register():
  form = RegisterForm(request.form)

  

  if form.validate_on_submit():
    # create a user instance not yet stored in the database
    user = User(name=form.name.data,
                email=form.email.data,
                password=generate_password_hash(form.password.data)
    )

    try:
      db.session.add(user)
      db.session.commit()
    except IntegrityError:
      flash('Check if your input is correct, else the username or email might already be in use.')
      return redirect(url_for('auth.register'))
      
    

    # Log the user in
    login_user(user)

    # flash will display a message to the user
    flash('Thanks for registering')
    # redirect user to the 'home' method of the user module
    return redirect(url_for('todo.index'))
  return render_template('auth/register.html', form=form)




@bp.route('/logout')
@login_required
def logout():
  logout_user()