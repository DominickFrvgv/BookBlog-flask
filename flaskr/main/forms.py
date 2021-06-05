from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import Length, DataRequired


class edit_Form(FlaskForm):
    about = TextAreaField('about me', validators=[Length(1, 115)])
    submit = SubmitField('update')

class book_Form(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(1, 80)])
    author = StringField('author', validators=[DataRequired(), Length(1, 80)])
    rating = IntegerField('rating')
    comment = TextAreaField('How was your expirience?')
    submit = SubmitField('Add Book')