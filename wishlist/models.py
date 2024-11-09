from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""Модель желаемого подарка"""


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    description = db.Column(db.String(300))
    price = db.Column(db.Integer)
    is_complete = db.Column(db.Boolean)
