from cProfile import label
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import Length, DataRequired

class ListsForm(FlaskForm):
    listname = StringField(label='List Name', validators=[Length(min=1, max=50), DataRequired()])
    submit = SubmitField(label='Add list')

class ItemForm(FlaskForm):
    itemname = StringField(label="Item Name", validators=[Length(min=1, max=50), DataRequired()])
    itemamount = IntegerField(label="Amount", validators=[DataRequired()])
    itempurchased = BooleanField(label=" 0-unpurchased, 1-purchased")
    itemowner = IntegerField(label="ID of list ", validators=[DataRequired()])
    submit = SubmitField(label='Add item')