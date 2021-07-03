from flask import Flask, render_template, url_for, flash, redirect
from main.forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from main import app
from main.models import User, Post


posts = [{

    'title': 'Blog post1',
    'author': 'Mahesh',
    'description': 'My first blog post',
    'date_added': 'June 1, 2021'
},
    {

        'title': 'Blog post2',
        'author': 'xyz',
        'description': 'My second blog post',
        'date_added': 'June 2, 2021'
    }
]


@app.route("/")
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title=about)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'''Account created for {form.username.data}!''', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title='Register', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please check Username and password', 'danger')

    return render_template("login.html", title='Login', form=form)
