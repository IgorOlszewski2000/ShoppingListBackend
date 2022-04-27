from email.policy import default
from lists import db

class Lists(db.Model): # database table for lists ex. lidl list or obi list
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    lista = db.relationship('List', backref='owned_user', lazy=True)

class List(db.Model): # database table for items ex. eggs or flowers 
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    amount = db.Column(db.Integer(), nullable=False)
    purchased = db.Column(db.Boolean(), default=False)
    owner = db.Column(db.Integer(), db.ForeignKey('lists.id')) # foregin key from Lists table

    def __repr__(self):
        return f'List {self.name}'