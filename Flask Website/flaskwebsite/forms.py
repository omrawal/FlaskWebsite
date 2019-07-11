from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flaskwebsite.models import Post


class ReviewForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    your_idea=TextAreaField('Share your review', validators=[DataRequired()])
    submit = SubmitField('Submit')
    #forms