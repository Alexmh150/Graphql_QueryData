import string
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserMixin

db = SQLAlchemy()

class Alumno(UserMixin, db.Model):
    __tablename__ = 'alumnos'
    partido = db.Column(db.String(50), primary_key = True)
    mediaAutoubicacion = db.Column(db.Float)
    votantes = db.Column(db.Integer)
    nsnc = db.Column(db.Integer)
