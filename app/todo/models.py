from app import db


class Todo(db.Model):

  __tablename__ = 'todos'

  id = db.Column(db.Integer, primary_key=True)
  body = db.Column(db.Text)
  priority = db.Column(db.String(50), default=None)
  tags = db.Column(db.String(50), default=None)
  done = db.Column(db.Boolean, default=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class Tag(db.Model):
  __talblename__ = 'tags'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))