from flask_restful import Resource


class DenysPage(Resource):

    def get(self):
        return "This is Denys s page"