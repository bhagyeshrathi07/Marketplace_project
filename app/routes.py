from flask_login import login_url
from app import myapp_obj
from flask import render_template

@myapp_obj.route("/login")
def loginPage():
    return render_template('home.html')