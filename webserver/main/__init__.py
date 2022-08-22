from flask import Flask
from flask_cors import CORS

import main.config
from main.models import init_database
from main.routes import Api, api


def create_app(config_name):
    global jwt
    app = Flask(__name__, template_folder='templates', static_url_path='')
    app.config.from_object(config.config_by_name[config_name])
    app.app_context().push()
    api.init_app(app)
    CORS(app)
    return app
