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
    itempurchased = BooleanField(label=" uncheck-unpurchased, check-purchased")
    itemowner = IntegerField(label="ID of list ", validators=[DataRequired()])
    submit = SubmitField(label='Add item')

class RemoveItemForm(FlaskForm):
    removeitemid = IntegerField(label="ID of item to remove", validators=[DataRequired()])
    submit = SubmitField(label="Remove Item")

class RemoveListForm(FlaskForm):
    removelistid = IntegerField(label="ID of list to remove", validators=[DataRequired()])
    submit = SubmitField(label="Remove List")

class ChangePurchasedForm(FlaskForm):
    itempurchasedid = IntegerField(label="ID of item", validators=[DataRequired()])
    submit = SubmitField(label="Accept")

class ChangeListsForm(FlaskForm):
    changelistid = IntegerField(label="ID of list to edit", validators=[DataRequired()])
    editname = StringField(label="New name of list", validators=[Length(min=1, max=50), DataRequired()])
    submit = SubmitField(label="Accept")
