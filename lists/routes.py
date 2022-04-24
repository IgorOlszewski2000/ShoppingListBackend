from lists import app
from flask import render_template, redirect, url_for
from lists.models import Lists, List
from lists.forms import ListsForm
from lists import db

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home_page():
    lists = Lists.query.all()
    list= List.query.all()
    return render_template('home.html', lists=lists, list=list)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/addlist', methods=['GET', 'POST'])
def addlist_page():
    form = ListsForm()
    if form.validate_on_submit():
        lists_to_create = Lists(name=form.listname.data)
        db.session.add(lists_to_create)
        db.session.commit()
        return redirect(url_for('home_page'))
    return render_template('addlist.html', form=form)