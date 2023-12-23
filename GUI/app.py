from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,SelectField
from wtforms.validators import DataRequired
import sys
import os
sys.path.insert(0, os.path.abspath('classes'))
import users
import pyodbc
connection=pyodbc.connect('Driver={SQL Server};SERVER=DESKTOP-9IHIA03;DATABASE=Coursiz;Trusted_Connection=yes')
cursor = connection.cursor()


app = Flask(__name__)
app.secret_key = 'super_secret_key'

class SignInForm(FlaskForm):
    Email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class SignUpForm(FlaskForm):
    Email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    type = SelectField(u'Type',choices=[('student', 'Student'), ('teacher', 'Teacher'), ('supervisor', 'Supervisor')], validators=[DataRequired()])
    submit = SubmitField('Sign Up')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Signin', methods=['GET', 'POST'])
def sign_in():
    form = SignInForm()

    if form.validate_on_submit():
        Email = form.Email.data
        password = form.password.data
        user=users.users()
        user.sign_in_values(Email,password)
        found=user.sign_in_validation()
        if found:
            flash('Sign In successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('Signin.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()

    if form.validate_on_submit():
        Email = form.Email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        type = form.type.data
        user=users.users()
        user.sign_up_values(Email,password,first_name,last_name,type)
        user.sign_up()
        flash(f'Email: {Email}, Password: {password} created successfully!', 'success')
        return redirect(url_for('sign_in'))

    return render_template('signup.html', form=form)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
