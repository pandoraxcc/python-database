import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Database setup

basedir = os.path.abspath(ox.path.dirname(__file__))
# __file__ --> app.py from the absolute path


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#############
# Creating model

db = SQLAlchemy(app)

class Cars( db.Model ):
    # Manual table name 
    __tablename__ = 'users'

    id = db.Column( db.Integer, primary_key = True )
    car_model = db.Column(db.Text)
    horse_power = db.Column(db.Integer)

    def __init__(self, car_model, horse_power):
        self.car_model = car_model
        self.horse_power = horse_power

    def __repr__(self):
        return f" Your car is {self.car_model} and has {self.horse_power}"
