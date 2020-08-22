from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,TextAreaField
from wtforms.validators import Email,DataRequired,Length


class MessageForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired(),Length(1,20)])
    body = TextAreaField('Message', validators = [DataRequired(),Length(1,200)])
    email = StringField('Email', validators = [DataRequired(),Length(1,64),Email(message = 'Your email is wrong, please try it again')])
    submit = SubmitField('Submit Request')