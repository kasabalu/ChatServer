from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError

class RegistrationForm(FlaskForm):
    """Registration form"""

    username = StringField('username_label', validators=[InputRequired(message="User Name Reauired"), Length(min=4, max=25, message = 'Must be 4 and 25 charc')])
    password = PasswordField("password_lable", validators=[InputRequired(message="Password Reauired"), Length(min=4, max=25, message = 'Must be 4 and 25 charc')])
    confirm_pswd = PasswordField('confirm_paswd_label', validators=[InputRequired(message="User Name Reauired"), EqualTo('password', message="password must Match")])

    submit_button= SubmitField('Create')

