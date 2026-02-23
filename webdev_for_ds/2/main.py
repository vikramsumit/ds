# from flask import Flask

# app = Flask(__name__)

# @app.route("/", methods = ["GET", "POST"])
# def hello_world():
#     return "<p>Hello, World!</p>"

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        subject = request.form.get("subject")
        message = request.form.get("message")

        print(full_name, email, phone, subject, message)

        return "Form Submitted Successfully!"

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)