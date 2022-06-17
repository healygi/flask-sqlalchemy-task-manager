from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")

@app.route("/catagories")
def catagories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("catagories.html", catagories=catagories)

@app.route("/add_catagories", methods=["GET", "POST"])
def add_catagories():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("catagories"))
    return render_template("add_catagories.html")