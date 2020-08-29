from flask import render_template
from fsm import app, config
import web

db = web.database(config.DATABASE_URL)

@app.route("/")
def index():
    fruits = db.select("fruits").list()
    return render_template("index.html", fruits=fruits)
