from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login = LoginManager()
admin = Admin()


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    return app


def initialize_extensions(app):
    db.init_app(app)
    login.init_app(app)
    admin.init_app(app)
    admin.name = "Quản lý bán hàng"
    admin.template_mode = "bootstrap4"


# app = Flask(__name__)
# app.secret_key = "<\x1e\xaa\xe5\xa8\xed\x9e\xf4\x0fC\xc8X_\xb4\x14x"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:15102000@localhost/saledbv1?charset=utf8mb4"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
#
#
# db = SQLAlchemy(app=app)
# admin = Admin(app=app, name="Quản lý bán hàng", template_mode="bootstrap4")
# login = LoginManager(app=app)
