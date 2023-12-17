from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'super_secret_key'

class SignInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Signin', methods=['GET', 'POST'])
def sign_in():
    form = SignInForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if username == "test" and password == "test":
            flash('Sign In successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('Signin.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        flash(f'Username: {username}, Password: {password} created successfully!', 'success')
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
