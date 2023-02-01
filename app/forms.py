from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length
from app.models import User
from flask_wtf.file import FileField,FileRequired,FileAllowed


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')


class AddbannerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    img = FileField('Image Banner', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif','jpeg'])])


class AddnewsForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    img = FileField('Image News', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif','jpeg'])])

class AddservicesForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    desc = TextAreaField('Description', validators=[DataRequired(), Length(min=1, max=240)])
    
class AddprojectsForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    desc = TextAreaField('Description', validators=[DataRequired(), Length(min=1, max=240)])
    img = FileField('Image Projects', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif','jpeg'])])

class AddvideosForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    video = FileField('Video News', validators=[FileRequired(), FileAllowed(['mp4', 'mov', 'webm','html5'])])
