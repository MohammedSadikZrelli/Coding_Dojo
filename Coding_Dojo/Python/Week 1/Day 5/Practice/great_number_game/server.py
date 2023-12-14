from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = "secret"


@app.route('/')
def index():
    # Generate a random number between 1 and 100
    session['target_number'] = random.randint(1, 100)
    return render_template("index.html", target_number=session['target_number'])


@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')


@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)