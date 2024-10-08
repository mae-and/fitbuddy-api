from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


class Class(db.Model):
    id = db.Ccdolumn(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(200))
    date_time = db.Column(db.String(50))
    capacity = db.Column(db.Integer, default=10)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('class_id'), nullable=False)
    status = db.Column(db.String(50), default="Pending")