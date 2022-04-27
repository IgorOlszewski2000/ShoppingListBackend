from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lists.db' #database config
app.config['SECRET_KEY'] = '3ee972ec770e08bfbdef61ba' #secrec key for database
db = SQLAlchemy(app)

from lists import routes