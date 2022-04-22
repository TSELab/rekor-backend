import json
import time

from flask_restful import Resource

from backend.models.entries import EntriesModel


class Entries(Resource):
    def get(self):
        newest_entry = EntriesModel.newest_entry()
        if not newest_entry:
            return {'message': 'Unable to get newest entry'}, 404
        payload =  newest_entry.json()
        idx = payload['idx']
        hash_val = json.loads(payload['payload'])['verification']['inclusionProof']['rootHash']
        time_epoch = int(time.time())
        return {'idx': idx, 'hashVal': hash_val, 'timeEpoch': time_epoch}
