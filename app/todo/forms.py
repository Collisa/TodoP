from flask_wtf import Form
from wtforms import TextField, SelectField, StringField
from .models import Tag

tag_choices = Tag.query.all()

class TodoForm(Form):
  body = TextField('add todo')
  priority = SelectField('Priority', choices=['High', 'Medium', 'Low'])
  tags = SelectField('Tags', choices=tag_choices)

class TagForm(Form):
  name = StringField('Tag name')