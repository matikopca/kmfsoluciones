from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# This list will act as a simple database for storing user credentials
users = [
    {'username': 'user1', 'password': 'password1'},
    {'username': 'user2', 'password': 'password2'},
    {'username': 'user3', 'password': 'password3'}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists and the password is correct
        for user in users:
            if user['username'] == username and user['password'] == password:
                return redirect(url_for('success'))
        
        # If user credentials are not found, display an error message
        error = 'Invalid username or password. Please try again.'
        return render_template('index.html', error=error)

    return render_template('index.html')

@app.route('/success')
def success():
    return 'Login successful!'

if __name__ == '__main__':
    app.run(debug=True)
