from lists import app
from flask import render_template
from lists.models import Lists
from lists.models import List

@app.route('/')
@app.route('/home')
def home_page():
    lists = Lists.query.all()
    list= List.query.all()
    return render_template('home.html', lists=lists, list=list)

@app.route('/about')
def about_page():
    return render_template('about.html')