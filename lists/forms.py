from cProfile import label
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired

class ListsForm(FlaskForm):
    listname = StringField(label='List Name', validators=[Length(min=1, max=50), DataRequired()])
    submit = SubmitField(label='Add list')

