from flask import Flask, render_template, request

app = Flask(__name__)

app.secret_key = "My_secret_key"

@app.route("/")
def hello_world():
    name = request.args.get("name")
    lang = request.args.get("lang")
    print(name, lang)
    # print(name)
    return render_template("index.html", lang = lang, name = name)

app.run(debug = True)