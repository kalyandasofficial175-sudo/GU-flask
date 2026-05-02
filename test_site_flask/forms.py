from flask_wtf import FlaskForm

from wtforms import StringField, EmailField, IntegerField, SelectField, RadioField,DateField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, NumberRange, Regexp

class TestForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[
        DataRequired(message="Email is required."),
        Regexp(
            r'^[\w\.-]+@gauhati\.ac\.in$', 
            message="Only @gauhati.ac.in emails are accepted."
        )
    ])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=1)])
    gender = SelectField('Gender', choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    
    ])

    religion = RadioField('Religion', choices=[
        ('H', 'Hindu'),
        ('M', 'Muslim'),
        ('O', 'Other')
    ])
    birthdate = DateField('Date of Birth', format='%Y-%m-%d', 
                          render_kw={"type": "date"}, 
                          validators=[DataRequired()
    ])
    
    profile_pic = FileField('Profile Picture', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'pdf'], 'Images and PDFs only!')
    ])
  