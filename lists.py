from enum import unique
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lists.db'
db = SQLAlchemy(app)

class Lists(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)

@app.route('/')
@app.route('/home')
def home_page():
    lists = Lists.query.all()
    return render_template('home.html', lists=lists)

@app.route('/about')
def about_page():
    return render_template('about.html')