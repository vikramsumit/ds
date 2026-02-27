from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():

    # aome mlm
    data = {"output": 45, "Accuracy": 98.8}
    return jsonify(data), 200

app.run(debug=True)