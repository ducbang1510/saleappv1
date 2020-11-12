from sqlalchemy import Integer, String, Float, Boolean, Column, ForeignKey, or_, and_
from sqlalchemy.orm import relationship
from flask_login import UserMixin, current_user, logout_user
from flask import redirect
from saleapp import db


class SaleBase(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __str__(self):
        return self.name


class User(SaleBase, UserMixin):
    __tablename__ = 'user'

    active = Column(Boolean, default=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)


class Category(SaleBase):
    __tablename__ = 'category'

    products = relationship('Product', backref='category', lazy=True)


class Product(SaleBase):
    __tablename__ = 'product'

    description = Column(String(255), nullable=True)
    price = Column(Float, default=0)
    image = Column(String(255), nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == "__main__":
    db.create_all()