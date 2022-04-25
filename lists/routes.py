from lists import app
from flask import render_template, redirect, request, url_for, flash
from lists.models import Lists, List
from lists.forms import ItemForm, ListsForm, RemoveItemForm, RemoveListForm
from lists import db
from sqlalchemy import select, update, delete, values

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

@app.route('/additem', methods=['GET', 'POST'])
def additem_page():
    form = ItemForm()
    if form.validate_on_submit():
        item_to_create = List(name=form.itemname.data,amount=form.itemamount.data,purchased=form.itempurchased.data,owner=form.itemowner.data)
        db.session.add(item_to_create)
        db.session.commit()
        return redirect(url_for('home_page'))
    return render_template('additem.html', form=form)

@app.route('/deleteitem.html', methods=['GET','POST'])
def deleteitem_page():
    form = RemoveItemForm()
    if form.validate_on_submit():
        itemm = form.removeitemid.data
        sql2 = delete(List).where(List.id == itemm)
        db.session.execute(sql2)
        db.session.commit()
        return redirect(url_for('home_page'))
    return render_template('/deleteitem.html', form=form)

@app.route('/deletelist.html', methods=['GET','POST'])
def deletelist_page():
    form = RemoveListForm()
    if form.validate_on_submit():
        listt = form.removelistid.data
        sql2 = delete(Lists).where(Lists.id == listt)
        db.session.execute(sql2)
        db.session.commit()
        return redirect(url_for('home_page'))
    return render_template('/deletelist.html', form=form)

# edit list
# remove list
# purchased item