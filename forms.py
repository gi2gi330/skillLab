from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField, FileField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo



class Addbookform(FlaskForm):
    name = StringField('name')
    img = FileField('image')
    pdf = FileField('pdf')
    submit = SubmitField('add book')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    repeat_password = PasswordField("Repeat Password",validators=[DataRequired(), EqualTo('password', message="not the same password")])
    submit = SubmitField("Register")
