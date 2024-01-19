from app import db

import string, secrets


class Gift(db.Model):
    __tablename__ = "gifts"

    id = db.Column(db.String(12), unique=True, nullable=False, primary_key=True)
    recipient_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    note = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(5), nullable=False)

    def __init__(self, recipient_id, note):
        uid = "".join(
            secrets.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(12)
        )

        while db.session.query(Gift).filter_by(id=uid).first() is not None:
            uid = "".join(
                secrets.choice(
                    string.ascii_uppercase + string.ascii_lowercase + string.digits
                )
                for _ in range(12)
            )

        self.id = uid
        self.recipient_id = recipient_id
        self.note = note
        self.code = "".join(secrets.choice(string.digits) for _ in range(3))

    def __repr__(self):
        return "<Gift %r>" % self.name

    def json(self):
        return {
            "id": self.id,
            "recipient_id": self.recipient_id,
            "note": self.note,
            "code": self.code,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
