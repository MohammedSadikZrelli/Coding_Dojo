from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user_model import User

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
     return render_template("dashboard.html")

@app.route("/add", methods=["post"])
def sam():
    print("🚀 "  *10, request.form, " 🚀   "*10)
    data = {**request.form}
    # session["username"]=request.form["first_name"]
    # print("++++++++++++++++++",session["username"])
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    session["email"] = request.form["email"]
    User.create(data)
    return redirect ("/dashboard")




