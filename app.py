from flask import Flask, render_template, send_from_directory
import os

app = Flask(
    __name__,
    template_folder="Templates"  # tell Flask to look for HTML here
)

# Serve static files from Templates/ as well
@app.route("/css/<path:filename>")
def css_files(filename):
    return send_from_directory(os.path.join("Templates", "css"), filename)

@app.route("/js/<path:filename>")
def js_files(filename):
    return send_from_directory(os.path.join("Templates", "js"), filename)

@app.route("/images/<path:filename>")
def image_files(filename):
    return send_from_directory(os.path.join("Templates", "images"), filename)

# 👇 Now your normal routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/categories")
def categories():
    return render_template("categories.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/merlin")
def merlin():
    return render_template("merlin.html")

@app.route("/products")
def products():
    return render_template("products.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
