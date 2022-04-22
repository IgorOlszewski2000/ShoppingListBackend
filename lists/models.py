from lists import db

class Lists(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)