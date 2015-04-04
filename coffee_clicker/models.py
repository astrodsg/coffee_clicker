from datetime import datetime
from coffee_clicker.database import db 


class User (db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    email = db.EmailField(unique=True)


class CaffineIntake (db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    name = 0
    caffine_amount = 0


class CaffineConsumption (db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    user = User 
    caffine_intake = CaffineIntake 
    number = 1
    timestamp = 0
