from flask import request

from app import db


class Session(db.Model):
    __tablename__ = "sessions"

    _count = 0

    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    token = db.Column(db.String(24), unique=True, nullable=False)

    def __init__(self, token, user_id):
        sessions = db.session.query(self.__class__).all()
        count = len(sessions)

        if count != 0:
            if sessions[-1].id >= Session._count:
                Session._count = sessions[-1].id + 1
            else:
                Session._count = count

        self.id = Session._count
        self.user_id = user_id
        self.token = token

        Session._count += 1

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
