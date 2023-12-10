from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'super_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin', methods=['POST'])
def sign_in():
    username = request.form['username']
    password = request.form['password']

    # Replace this with your authentication logic
    if username == "k" and password == "Kimo gamed fa45":
        flash('Sign In successful!', 'success')
    else:
        flash('Invalid username or password', 'error')

    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Replace this with your sign-up logic
        flash(f'Username: {username}, Password: {password} created successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
