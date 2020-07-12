from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from resources.denys_page import DenysPage
from resources.main import Main
from resources.health import Health


app = Flask(__name__)
CORS(app)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = "InPythonWeTrust13!"
app.config["JWT_HEADER_TYPE"] = ""
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
api = Api(app)

jwt = JWTManager(app)


@jwt.user_claims_loader
def add_claims_to_access_token(user):
    return user.email


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


url = "/api/v1"
api.add_resource(Health, "/health")
api.add_resource(Main, "/")
api.add_resource(DenysPage, "/pages/DanysPage")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
