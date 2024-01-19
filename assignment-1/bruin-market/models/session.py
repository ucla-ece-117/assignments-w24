from flask import request

from app import db

import string, secrets


class Session(db.Model):
    __tablename__ = "sessions"

    id = db.Column(db.String(12), unique=True, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    token = db.Column(db.String(24), unique=True, nullable=False)

    def __init__(self, token, user_id):
        uid = "".join(
            secrets.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(12)
        )

        while db.session.query(Session).filter_by(id=uid).first() is not None:
            uid = "".join(
                secrets.choice(
                    string.ascii_uppercase + string.ascii_lowercase + string.digits
                )
                for _ in range(12)
            )

        self.id = uid
        self.user_id = user_id
        self.token = token

    def __repr__(self):
        return "<Session %r>" % self.token

    def json(self):
        return {"id": self.id, "token": self.token, "user_id": self.user_id}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


def is_session_valid():
    token = request.cookies.get("session")
    from app import app, db

    with app.app_context():
        exists = (
            db.session.query(Session.token).filter_by(token=token).scalar() is not None
        )
        if exists:
            return True
        return False
