from cProfile import label
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import Length, DataRequired

class ListsForm(FlaskForm):
    listname = StringField(label='LIST NAME', validators=[Length(min=1, max=50), DataRequired()])
    submit = SubmitField(label='ACCEPT')

class ItemForm(FlaskForm):
    itemname = StringField(label="ITEM NAME", validators=[Length(min=1, max=50), DataRequired()])
    itemamount = IntegerField(label="AMOUNT", validators=[DataRequired()])
    itempurchased = BooleanField(label="UNCHECK-UNPURCHASED, CHECK-PURCHASED")
    itemowner = IntegerField(label="ID OF LIST", validators=[DataRequired()])
    submit = SubmitField(label='ACCEPT')

class RemoveItemForm(FlaskForm):
    removeitemid = IntegerField(label="ID OF ITEM TO REMOVE", validators=[DataRequired()])
    submit = SubmitField(label="ACCEPT")

class RemoveListForm(FlaskForm):
    removelistid = IntegerField(label="ID OF LIST TO REMOVE", validators=[DataRequired()])
    submit = SubmitField(label="ACCEPT")

class ChangePurchasedForm(FlaskForm):
    itempurchasedid = IntegerField(label="ID OF ITEM TO CHANGE", validators=[DataRequired()])
    submit = SubmitField(label="ACCEPT")

class ChangeListsForm(FlaskForm):
    changelistid = IntegerField(label="ID OF LIST TO EDIT", validators=[DataRequired()])
    editname = StringField(label="NEW NAME OF LIST", validators=[Length(min=1, max=50), DataRequired()])
    submit = SubmitField(label="ACCEPT")
