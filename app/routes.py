from flask import Flask, render_template


def load(app: Flask) -> Flask:
    @app.route("/")
    def home():
        name = "Hello World!"
        return render_template("home.html", name=name)
    
    @app.route("/login")
    def login():
        return render_template('login.html')
    
    return app
    