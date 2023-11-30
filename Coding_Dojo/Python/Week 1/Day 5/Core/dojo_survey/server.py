from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change this to a more secure key in a real-world scenario

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Retrieve form data
    name = request.form['name']
    email = request.form['email']
    # Store form data in session
    session['name'] = name
    session['email'] = email
    return redirect('/result')

@app.route('/result')
def result():
    # Retrieve form data from session
    name = session['name']
    email = session['email']
    return render_template('result.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)