from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5

admin_email = "admin@email.com"
admin_password = "12345678"

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[validators.Length(min=6, max=120), validators.Email()])
    password = PasswordField(label='Password', validators=[validators.Length(min=6, max=120)])
    submit = SubmitField(label="Log In")

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "any-string-you-want-just-keep-it-secret"


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if admin_password == login_form.password.data and admin_email == login_form.email.data:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)



if __name__ == '__main__':
    app.run(debug=True)
