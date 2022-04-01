from backend.db import db


class StatsModel(db.Model):
    __bind_key__ = None

    idx = db.Column(db.Integer, primary_key=True)
    payload = db.Column(db.Text)

    def __repr__(self):
        return f'Stats {self.idx}'

    @classmethod
    def newest_entry(cls):
        print(cls.query.filter_by(idx=1).first())
        return {'this': 'is a test'}
