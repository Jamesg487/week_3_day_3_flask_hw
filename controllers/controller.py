from flask import render_template
from app import app
from models.orders_list import orders

@app.route("/orders")
def Orders():
    return render_template("index.html", title="Orders", orders=orders)

@app.route("/orders/<index>")
def order(index):
    order = orders[int(index)]
    return render_template("order.html", title=f"Order Number {index}", order=order)
