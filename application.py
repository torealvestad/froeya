from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/my_activities")
def my_activities():
    return render_template("my_activities.html")
