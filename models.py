from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Example(db.Model):
    __tablename__ = "Examples"

    id = db.Column(db.Integer, primary_key=True, unique=True)