from flask import Flask
from flask_restful import Api
from api import Book

app = Flask(__name__)
api = Api(app)

# 필수 설정들
app.config["API_TITLE"] = "Book Store API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/apidocs"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


api.add_resource(Book, '/book/<string:name>' )
