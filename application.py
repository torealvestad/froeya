import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/my_activities")
def activities():
    return render_template("my_activities.html")

@app.route("/friends")
def friends():

    return render_template("friends.html")

@app.route("/music")
def music():
    return render_template("music.html")

@app.route("/birthday")
def birthday():
    now = datetime.datetime.now()
    my_birthday = now.month == 12 and now.day == 24
    return render_template("birthday.html", my_birthday = my_birthday)
