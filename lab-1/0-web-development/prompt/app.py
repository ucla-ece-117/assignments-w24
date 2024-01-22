from flask import Flask, send_from_directory, request, make_response

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "password123"


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("static", path)


@app.route("/auth", methods=["POST"])
def auth():
    username = request.form["username"]
    password = request.form["password"]

    if username != USERNAME or password != PASSWORD:
        return "Invalid Credentials", 401

    res = make_response("Logged In")
    res.set_cookie("auth", "True")
    return res, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
