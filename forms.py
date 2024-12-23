from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField, FileField
from wtforms.validators import DataRequired



class Addbookform(FlaskForm):
    name = StringField('name')
    img = StringField('image')
    
    submit = SubmitField('add book')
