from flask_restful import Resource
from datetime import datetime


class Main(Resource):

    def get(self):
        return f"Test {datetime.now()}"
