from app import db


class Todo(db.Model):

  __tablename__ = 'todos'

  id = db.Column(db.Integer, primary_key=True)
  body = db.Column(db.Text)
  priority = db.Column(db.String(50))
  tags = db.Column(db.String(50))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)