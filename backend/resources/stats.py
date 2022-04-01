from flask_restful import Resource 

from backend.models.stats import StatsModel


class Stats(Resource):
    def get(self):
        return StatsModel.newest_entry()
