import os
from flask import Flask, render_template

from config import basedir


def create_app():
    app = Flask(__name__,
        template_folder=os.path.join(basedir, "resources", "templates"), # => Config para reconehcer diretório templates
        static_folder=os.path.join(basedir, "resources", "static") # => Config para reconehcer diretório static
        )

    from app import routes
    routes.load(app)

    from app.filters import text_truncate
    app.jinja_env.filters["text_truncate"] = text_truncate

    return app
