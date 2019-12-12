from flask import Flask, render_template, url_for


def load(app: Flask) -> Flask:
#    @app.route("/")
#    def home():
#        name = "Hello World!"
#        return render_template("home.html", name=name)
    
    @app.route("/")
    @app.route("/dashboard")
    def dashboard():
        return render_template("auth/dashboard.html")

    @app.route("/dashboard/new_Ticket")
    def new_Ticket():
        return render_template("auth/new_ticket.html")

    @app.route("/dashboard/update_Ticket")
    def update_Ticket():
        return render_template, url_for("auth/dashboard/snippets/update.html")

    @app.route("/dashboard/delete_Ticket")
    def update_Ticket():
        return render_template, url_for("auth/dashboard/snippets/delete.html")

    @app.route("/signin")
    def signin():
        return render_template("signin.html")
    
    @app.route("signup")
    def signup():
        return render_template("signup.html")
    
    return app
    