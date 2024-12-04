from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string
import random
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_number = db.Column(db.String(120), unique=True, nullable=False)
    device_number = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    battery_type = db.Column(db.String(120), default="Lead Acid")
    battery_voltage = db.Column(db.String(120), default="12")
    battery_capacity = db.Column(db.String(120), default="1000")
    battery_model = db.Column(db.String(120), default="None")


    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    Batteries = db.relationship('Battery', backref="user")

    def __repr__(self) -> str:
        return 'User>>> {self.username}'


class Battery(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    voltage = db.Column(db.Text, default=0)
    current = db.Column(db.Text, default=0)
    SOC = db.Column(db.Text, default=0)
    SOH = db.Column(db.Text, default=0)
    RUL_EOL = db.Column(db.Text, default=0)
    DOD = db.Column(db.Text, default=0)
    brand = db.Column(db.Text, default=0)
    capacity = db.Column(db.Text, default=0)
    no_load_v = db.Column(db.Text, default=0)
    internal_resistance = db.Column(db.Text, default=0)
    number_of_cycle = db.Column(db.Text, default=0)
    
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())


    def __repr__(self) -> str:
        return 'Boomark>>> {self.url}'