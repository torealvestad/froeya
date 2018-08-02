import datetime

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/my_activities")
def activities():
    return render_template("my_activities.html")

@app.route("/friends")
def friends():

    pictures = ["sanne_linde.jpg", "julia.jpg","alva.jpg", "emilie.jpg","kira_lea.jpg"]
    names = ["Sanne", "Linde", "Petter"]

    return render_template("friends.html", pictures=pictures, names=names)

@app.route("/music")
def music():
    return render_template("music.html")

@app.route("/birthday")
def birthday():
    now = datetime.datetime.now()
    my_birthday = now.month == 12 and now.day == 24
    return render_template("birthday.html", my_birthday = my_birthday)

@app.route("/memoirs", methods=["POST", "GET"])
def memoirs():
    if request.method == "GET":
        return render_template("memoirs.html")
    else:
        story = request.form.get("story")
        return render_template("memoirs.html", story=story)
