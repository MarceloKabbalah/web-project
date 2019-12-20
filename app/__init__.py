import os
from flask import Flask, app, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from settings import BASE_DIR, SECRET_KEY



app = Flask(__name__,
    template_folder=os.path.join(BASE_DIR, "resources", "templates"),
    static_folder=os.path.join(BASE_DIR, "resources", "static")
    )
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app.controllers import routes
routes.load(app)


