from flask import Flask, render_template, make_response, abort
import os, random, subprocess
from random import shuffle
from datetime import date

listofffiles = [i[:-5] if i.endswith(".html") else i for i in os.listdir("templates")]

analog_path = "static/media/gallery/analog/"
digital_path = "static/media/gallery/digital/"

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
    def homelab():
        return render_template("pages/homelab.html")

    @app.route("/contact")
    def contact():
        return render_template("pages/contact.html")

    @app.route("/portfolio")
    def portfolio():
        return render_template("pages/portfolio.html")
        
    @app.route("/photography")
    def photography():
        return render_template("pages/photography.html", analog_gallery = get_images(analog_path), digital_gallery = get_images(digital_path))

    return app

def get_age():
    today = date.today()
    born = date(2004, 2, 23)
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return age

def get_images(path):
    gallery = []
    for image in os.listdir(path):
        if image.endswith(".optimized.webp"):
            gallery.append(image)

        else:
            if image.endswith((".JPG", ".jpeg")):
                filename, extension = os.path.splitext(image)
                new_file_extension = "".join([filename, ".jpg"])
                os.rename(os.path.join(path, image), os.path.join(path, new_file_extension))
                image = new_file_extension

            if image.endswith(".jpg"):
                thumbnail = image.replace(".jpg", ".optimized.webp")
                thumbnail_path = os.path.join(path, thumbnail)
                if not os.path.isfile(thumbnail_path):
                    image_path = os.path.join(path, image)
                    subprocess.run(["convert", image_path, "-resize", "600x400", thumbnail_path])
                    gallery.append(thumbnail)

    shuffle(gallery)
    return gallery
