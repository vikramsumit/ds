from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = "johnwick"
    language = "PYthon"
    luckynos = [1,2,4,546,65,32,12]
    # footer = "<p style> This one is not the last movie of johnn wick </p>"
    footer = """<p style="color: white; background-color: black; font-size: 18px; padding: 10px; border-radius: 5px;">
    This one is not the last movie of John Wick</p>"""

    return render_template("index.html", name=name, lang = language, lucky = luckynos, footer = footer)

app.run(debug=True)