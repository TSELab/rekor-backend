from backend.db import db


class EntriesModel(db.Model):
    __bind_key__ = None
    __tablename__ = 'entries'

    idx = db.Column(db.Integer, primary_key=True)
    payload = db.Column(db.Text)

    def __repr__(self):
        return f'Stats {self.idx}'

    def json(self):
        return {'idx': self.idx, 'payload': self.payload}

    @classmethod
    def newest_entry(cls):
        return cls.query.order_by(cls.idx.desc()).first()
