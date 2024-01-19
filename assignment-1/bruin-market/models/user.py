from app import db


import string, secrets


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(12), unique=True, nullable=False, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    balance = db.Column(db.Float(precision=2), nullable=False)

    def __init__(self, username, password):
        uid = "".join(
            secrets.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(12)
        )

        while db.session.query(User).filter_by(id=uid).first() is not None:
            uid = "".join(
                secrets.choice(
                    string.ascii_uppercase + string.ascii_lowercase + string.digits
                )
                for _ in range(12)
            )

        self.id = uid
        self.username = username
        self.password = password
        self.balance = 1000.0

    def __repr__(self):
        return "<User %r>" % self.username

    def json(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "balance": self.balance,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
