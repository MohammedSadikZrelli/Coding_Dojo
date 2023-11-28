from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
     return render_template("dashboard.html")

@app.route("/register", methods=["post"])
def register():
    print("🚀 "  *10, request.form, " 🚀   "*10)
    data = {**request.form}
    session["username"]=request.form["first_name"]
    print("++++++++++++++++++",session["username"])
    if User.validate(data):
        pw_hash=bcrypt.generate_password_hash(data["password"])
        data["password"]=pw_hash
        User.create(data)
    return redirect ("/")

@app.route("/login", methods=["post"])
def login():
    user_in_db = User.get_one_by_email({"email": request.form["email"]})
    print("++++++++++++++++++",user_in_db)
    session["username"].upper=user_in_db["first_name"]+" "+user_in_db["last_name"]
    print("++++++++++++++++++",session["username"])
    
    if not user_in_db:
        flash("Email does't exist.")
        return redirect("/","login")
    if not bcrypt.check_password_hash(user_in_db["password"], request.form["password"]):
        # if we get False after checking the password
        flash("Invalid Password","login")
        return redirect("/")
    return redirect("/dashboard")
