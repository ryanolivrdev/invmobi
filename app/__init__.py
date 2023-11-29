from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@172.23.176.1:5432/flask_db"
app.config['SECRET_KEY'] = "mysecret"

login_manager = LoginManager(app)
login_manager.login_view = "signin"
db = SQLAlchemy(app)