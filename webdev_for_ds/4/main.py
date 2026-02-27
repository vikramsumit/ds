from flask import Flask, render_template, flash

app = Flask(__name__)

app.secret_key = 'My_secret_key'

@app.route("/")
def home():
    flash("Thank You for visiting my web page")
    return render_template("index.html")

@app.route("/about")
def about():
    flash("THanks for visiting about page")
    return render_template("about.html") 

@app.route("/contact")
def contact():
    return render_template("contact.html")

app.run(debug = True)
