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

@app.route("/manage-stock", methods=['GET', 'POST'])
def manage_stock():
    if request.method == 'POST':
        form = request.form
        type, id, quantity = form['type'], form['fruit'], float(form['quantity'])
        fruit = db.select("fruits",
            where="id=$id",
            vars={"id": int(id)}
        ).first()

        new_quantity = fruit.quantity + quantity if type=='add' else fruit.quantity - quantity

        db.update("fruits",
            quantity = new_quantity,
            where="id=$id",
            vars={"id": id})

        flash(f"{new_quantity} Kgs of {fruit.name} is available.")
        return redirect(url_for("index"))

    fruits = db.select("fruits").list()
    return render_template("manage_stock.html", fruits = fruits)
