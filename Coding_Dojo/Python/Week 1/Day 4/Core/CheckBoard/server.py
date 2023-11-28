from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkboard():
    return render_template("index.html")

@app.route('/<int:x>')
def check_x(x):
    return render_template("index.html",x=x)

@app.route('/<int:x>/<int:y>')
def check_x_y(x, y):
    return render_template("index.html", x=x, y=y)

if __name__ == "__main__":
    app.run(debug=True)