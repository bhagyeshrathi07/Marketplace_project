from __init__ import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), nullable=False, index=True, unique=True)
	password_hash = db.Column(db.String(128), nullable=False)

	def __repr__(self):
		return f'User {self.username}'

class Item(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(64), nullable=False, unique=True)
	price = db.Column(db.Integer(), nullable=False)
	description = db.Column(db.String(1024), nullable=False, unique=True)

	def __repr__(self):
    		return f'Item {self.name}'
