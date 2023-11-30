from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo_model import Dojo

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html",)


@app.route("/process", methods=["post"])
def register():
    print("🚀 "  *10, request.form, " 🚀   "*10)
    # if User.validate(requ)
    data = {**request.form}
    if (Dojo.create(data)):
        return redirect("/dashboard")
    return redirect("/")


@app.route("/login", methods=["post"])
def login():
    user_in_db = Dojo.get_one_by_email({"email": request.form["email"]})
    if not user_in_db:
        flash("Email does't exist.")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        # if we get False after checking the password
        flash("Invalid Password")
        return redirect("/")
    return redirect("/dashboard")