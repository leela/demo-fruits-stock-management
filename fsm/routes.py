from flask import render_template
from fsm import app

@app.route("/")
def index():
    fruits = [
        {'name': 'Banana', 'price': 20.0, 'quantity': 100},
        {'name': 'Apple', 'price': 100.0, 'quantity': 50},
        {'name': 'Guava', 'price': 40.0, 'quantity': 120},
        {'name': 'Pomegranate', 'price': 60.0, 'quantity': 200},
    ]
    return render_template("index.html", fruits=fruits)
