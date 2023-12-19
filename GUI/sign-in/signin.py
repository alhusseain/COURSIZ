from flask import Flask, render_template, request, redirect, url_for, flash
import datetime
app = Flask(__name__)
app.secret_key = 'super_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin', methods=['POST'])
def sign_in():
    username = request.form['username']
    password = request.form['password']

    if username == "Test" and password == "K.test":
        flash('Sign In successful!', 'success')
    else:
        flash('Invalid username or password', 'error')

    return redirect(url_for('index'))

# users must choose whether they are students or teachers
# it must be able to insert the data into the database
# it must be able to check if the data is valid (username must be unique, password must be strong using regex, email must be valid using regex)
# it must store the account creation date and time
@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        flash(f'Username: {username}, Email: {email},Password: {password} created successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
