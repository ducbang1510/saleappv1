import json
from saleapp import db
from saleapp.models import *

# def read_data(path='data/categories.json'):
#     with open(path, encoding='utf-8') as f:
#         return json.load(f)

def read_category():
    return Category.query.all()


def get_product_by_id(product_id):
    # products = read_data('data/products.json')
    return Product.query.get(product_id)
    # for p in products:
    #     if p["id"] == product_id:
    #         return p


def read_products(kw=None, cate_id=None,
                  from_price=None, to_price=None):
    products = Product.query
    if cate_id:
        products = products.join(Category, Category.id == Product.category_id) \
                .filter(Product.category_id == cate_id)
        # cate_id = int(cate_id)
        # products = [p for p in products if (p['category_id'] == cate_id)]

    if kw:
        products = products.filter(Product.name.contains(kw))
        # products = [p for p in products if p['name'].find(kw) >= 0]

    if from_price and to_price:
        products = products.filter(Product.price.__gt__(from_price), Product.price.__lt__(to_price))
        # from_price = float(from_price)
        # to_price = float(to_price)
        # products = [p for p in products if p['price'] >= from_price and p['price'] <= to_price]

    return products.all()
