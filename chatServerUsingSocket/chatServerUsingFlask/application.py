from flask import Flask, render_template, redirect, url_for
from wtform_fileds import *
import pymysql
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key= "mysecret"

app.config['MYSQL_HOST']= '127.0.0.1'
app.config['MYSQL_PORT']= 3306
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_DB']= 'test'
app.config["MYSQL_CURSORCLASS"]="DictCursor"

#get this from vault
app.config['MYSQL_PASSWORD']= 'xxx'
mysql = MySQL(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data
        cur = mysql.connection.cursor()

        inserQuery = """insert into users(username, password) values ("{0}", "{1}")""".format(username, password)
        rows = cur.execute(inserQuery)
        print(rows)
        if rows == 1:
            mysql.connection.commit()
            return redirect(url_for('login'))

    return render_template("index.html",form=reg_form)

@app.route("/login", methods=['GET', 'POST'])
def login():

    login_form = LoginForm()

    # Allow login if validation success
    if login_form.validate_on_submit():
        return "Logged In"

    # for Get method
    return render_template("login.html", form=login_form)

if __name__ == "__main__":
    app.run(debug=True)
