from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = "<\x1e\xaa\xe5\xa8\xed\x9e\xf4\x0fC\xc8X_\xb4\x14x"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:15102000@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)
admin = Admin(app=app, name="Quản lý bán hàng", template_mode="bootstrap4")
login = LoginManager(app=app)
