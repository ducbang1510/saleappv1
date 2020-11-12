from flask import render_template, request, redirect
from saleapp import app, utils, admins, login
from flask_login import login_user
from saleapp.models import *
import hashlib


@app.route("/")
def index():
    categories = utils.read_data()
    return render_template('index.html',
                           categories=categories)


@app.route("/products")
def product_list():
    kw = request.args.get("kw")
    cate_id = request.args.get("category_id")
    from_price = request.args.get("from_price")
    to_price = request.args.get("to_price")

    products = utils.read_products(cate_id=cate_id,
                                   kw=kw,
                                   from_price=from_price,
                                   to_price=to_price)

    return render_template('products.html',
                           products=products)


@app.route("/products/<int:product_id>")
def product_detail(product_id):
    product = utils.get_product_by_id(product_id=product_id)

    return render_template('product_detail.html',
                           product=product)


@app.route("/login-admin", methods=["post", "get"])
def login_admin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password", "")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        user = User.query.filter(User.username == username.strip(), User.password == password).first()

        if user:
            login_user(user=user)

    return redirect("/admin")


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    app.run(debug=True)