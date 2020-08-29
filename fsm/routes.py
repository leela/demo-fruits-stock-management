from flask import (render_template, url_for, request, flash,
    redirect)
from fsm import app, config
import web

db = web.database(config.DATABASE_URL)

@app.route("/")
def index():
    fruits = db.select("fruits").list()
    return render_template("index.html", fruits=fruits)

@app.route("/fruits", methods=['GET', 'POST'])
def fruits():
    if request.method == 'POST':
        name, price = request.form['fruit'], request.form['price']
        db.insert("fruits", name=name, price= float(price))
        flash(f"Fruit {name} Added to the system")
        return redirect(url_for("index"))
    return render_template("add_fruit.html")
