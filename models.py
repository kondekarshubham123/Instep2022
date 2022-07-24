import datetime
from random import randint
from flask_login import UserMixin
from __init__ import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    registration_type = db.Column(db.String(100))

class Drugs(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    drug_name = db.Column(db.String(100))
    drug_indication = db.Column(db.String(100))
    drug_details = db.Column(db.String(1000))
    drug_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    drug_process = db.Column(db.Integer, default=randint(0,100))