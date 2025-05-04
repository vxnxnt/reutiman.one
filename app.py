from flask import Flask, render_template, make_response, abort
import os, random
from datetime import date

listofffiles = [i[:-5] if i.endswith(".html") else i for i in os.listdir("templates")]

def create_app():
    app = Flask(__name__)

    @app.errorhandler(403)
    def forbidden403(e):
        return make_response(render_template("error_pages/403.html"), 403)

    @app.errorhandler(404)
    def notfound404(e):
        return make_response(render_template("error_pages/404.html"), 404)

    @app.route("/whatever")
    def ellmao():
        abort(403)

    @app.route("/")
    def index():
        return render_template("pages/index.html", age = get_age())

    @app.route("/homelab")
    def blog():
        return render_template("pages/homelab.html")

    @app.route("/contact")
    def contact():
        return render_template("pages/contact.html")

    @app.route("/portfolio")
    def other():
        return render_template("pages/portfolio.html")

    return app

# create_app().run(debug=True)

def get_age():
    today = date.today()
    born = date(2004, 2, 23)
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return age
