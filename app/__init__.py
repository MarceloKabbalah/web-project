import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from settings import BASE_DIR
from app.controllers import routes


def create_app():
    app = Flask(__name__,
        template_folder=os.path.join(BASE_DIR, "resources", "templates"), # => Config para reconehcer diretório templates
        static_folder=os.path.join(BASE_DIR, "resources", "static") # => Config para reconehcer diretório static
        
        )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATBASE_URI'] = 'sqlite:///test.sqlite3'
    db = SQLAlchemy(app)
    
    from app import routes
    routes.load(app)

    from app.filters import text_truncate
    app.jinja_env.filters["text_truncate"] = text_truncate

    return app
