from flask import jsonify, request


def router():
    if request.method == "POST":
        return post()

    res = {"status": "Unsupported HTTP request method."}

    return jsonify(res), 500


def post():
    data = request.json
    recipient = data.get("recipient")
    note = data.get("note")

    res = {"status": ""}

    if recipient is None or note is None:
        res["status"] = "Both `name` and `price` are required."
        return jsonify(res), 400

    from app import app, db
    from models.gift import Gift

    with app.app_context():
        from models.user import User

        recipient = db.session.query(User).filter_by(username=recipient).first()

        if recipient is None:
            res["status"] = "Recipient not found."
            return jsonify(res), 404

        gift = Gift(recipient.id, note)
        gift.save_to_db()

        res["status"] = "Success."
        res["gift"] = gift.json()
        del res["gift"]["code"]

        return jsonify(res), 201
