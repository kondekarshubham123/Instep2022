import datetime
from random import randint
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from __init__ import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    registration_type = db.Column(db.String(100))

    def __init__(self,email,password,name,registration_type) -> None:
        self.email=email
        self.password=password
        self.name=name
        self.registration_type=registration_type
    
    @staticmethod
    def create(email,password,name,registration_type):
        new_user = User(email,generate_password_hash(password, method='sha256'),name,registration_type)
        db.session.add(new_user)
        db.session.commit()

class Drugs(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    drug_name = db.Column(db.String(100))
    drug_indication = db.Column(db.String(100))
    drug_details = db.Column(db.String(1000))
    drug_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    drug_process = db.Column(db.Integer)

    def __init__(self,drug_name,drug_indication,drug_details,drug_process) -> None:
        self.drug_name = drug_name
        self.drug_indication = drug_indication
        self.drug_details = drug_details
        self.drug_process = drug_process

    @staticmethod
    def create(drug_name,drug_indication,drug_details):
        new_drug = Drugs(drug_name,drug_indication,drug_details,randint(0,100))
        db.session.add(new_drug)
        db.session.commit()