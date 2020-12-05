from flask_wtf import Form
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required, EqualTo, Email

class LoginForm(Form):
  email = TextField('Email address', [Required(), Email()])
  password = PasswordField('Password', [Required()])
  remember = BooleanField('Remember me')

class RegisterForm(Form):
  name = TextField('Username', [Required()])
  email = TextField('Email address', [Required(), Email()])
  password = PasswordField('Password', [Required()])
  confirm = PasswordField('Repeat Password', [
    Required(),
    EqualTo('password', message='Passwords must match')
  ])
