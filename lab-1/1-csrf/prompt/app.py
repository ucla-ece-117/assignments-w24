from flask import Flask, render_template, make_response, request

app = Flask(__name__)

username = "admin"
balance = 1000


@app.route("/")
def index():
    auth = request.cookies.get("auth")
    res = make_response(
        render_template("index.html", auth=auth, username=username, balance=balance)
    )
    return res, 200


@app.route("/username", methods=["GET"])
def change_username():
    global username
    new_username = request.args.get("username") or username
    username = new_username
    res = make_response({"username": username})
    return res, 200


@app.route("/balance", methods=["POST"])
def get_balance():
    if request.cookies.get("auth") != "true":
        return make_response({"error": "Not authenticated"}), 401

    amount = request.form.get("amount")
    global balance
    balance += int(amount)

    res = make_response({"balance": balance})
    return res, 200


@app.route("/auth", methods=["POST"])
def auth():
    request
    res = make_response({"success": True})
    res.headers["Set-Cookie"] = "auth=true; HttpOnly; SameSite=None; Secure"
    return res, 200
