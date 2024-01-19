from flask import request, jsonify

import re


def transfer():
    from models.session import Session
    from models.user import User

    from app import app, db

    res = {"status": ""}

    receiver_username = ""
    amount = ""

    if request.content_type == "application/x-www-form-urlencoded":
        receiver_username = request.form.get("receiver")
        amount = request.form.get("amount")
    else:
        data = request.json
        receiver_username = data.get("receiver")
        amount = data.get("amount")

    if receiver_username is None or amount is None:
        res["status"] = "Both `receiver` and `amount` are required."
        return jsonify(res), 400

    if not re.search(r"^(0|[1-9][0-9]{0,2})(,\d{3})*(\.\d{1,2})?$", amount):
        res["status"] = "Invalid amount."
        return jsonify(res), 400

    amount = float(amount)

    if amount <= 0:
        res["status"] = "Amount must be greater than 0."
        return jsonify(res), 400

    with app.app_context():
        token = request.cookies.get("session")
        session = db.session.query(Session).filter_by(token=token).first()
        sender = db.session.query(User).filter_by(id=session.user_id).first()

        if sender is None:
            res["status"] = "Sender not found."
            return jsonify(res), 404

        receiver = db.session.query(User).filter_by(username=receiver_username).first()

        if receiver is None:
            res["status"] = "Receiver not found."
            return jsonify(res), 404

        if sender.balance < amount:
            res["status"] = "Insufficient balance."
            return jsonify(res), 400

        sender.balance -= amount
        sender.save_to_db()

        receiver.balance += amount
        receiver.save_to_db()

        res["status"] = "Success."
        res["sender"] = sender.json()

        return jsonify(res), 201
