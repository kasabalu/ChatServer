from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from application import mysql

def invalid_credentials(form, field):
    """ Username and password checker """

    password = field.data
    username = form.username.data

    # Check username is invalid
    cur = mysql.connection.cursor()
    userQuery = """select * from users where username = "{0}" """.format(username)
    print(userQuery)
    rows = cur.execute(userQuery)
    rv = cur.fetchone()
    #print(rv['password'])
    if rows == 0:
        raise ValidationError(" Invalid User Name")
    elif password != rv['password']:
        raise ValidationError(" Incorrect Password")


    """"
    # Check password in invalid
    elif not pbkdf2_sha256.verify(password, user_data.hashed_pswd):
        raise ValidationError("Username or password is incorrect")
    """
class RegistrationForm(FlaskForm):
    """Registration form"""

    username = StringField('username_label', validators=[InputRequired(message="User Name Required"), Length(min=4, max=25, message = 'Must be 4 and 25 charc')])
    password = PasswordField("password_label", validators=[InputRequired(message="Password Required"), Length(min=4, max=25, message = 'Must be 4 and 25 charc')])
    confirm_pswd = PasswordField('confirm_paswd_label', validators=[InputRequired(message="User Name Reauired"), EqualTo('password', message="password must Match")])

    submit_button= SubmitField('Create')

    def validate_username(self, username):
        cur = mysql.connection.cursor()
        userQuery = """select * from users where username = "{0}" """.format(username.data)
        print(userQuery)
        rows = cur.execute(userQuery)
        if rows == 1:
            raise  ValidationError(" User name already exists, Select different username")

class LoginForm(FlaskForm):
    """

    """
    username = StringField('username_label', validators=[InputRequired(message="User Name Required")])
    password = PasswordField("password_label", validators=[InputRequired(message="Password Required"), invalid_credentials])






