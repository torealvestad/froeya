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
