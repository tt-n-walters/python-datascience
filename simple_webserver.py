import flask


app = flask.Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome!"


@app.route("/message", methods=["POST"])
def post_message():
    name = flask.request.form.get("name")
    text = flask.request.form.get("text")
    print(name, "says:", text)
    return "message sent"


app.run(host="0.0.0.0")
