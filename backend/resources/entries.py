from flask_restful import Resource

from backend.models.entries import EntriesModel


class Entries(Resource):
    def get(self):
        newest_entry = EntriesModel.newest_entry()
        if not newest_entry:
            return {'message': 'Unable to get newest entry'}, 404
        return newest_entry.json()
