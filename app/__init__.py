from flask import Flask
from openbrokerapi import api
from openbrokerapi.log_util import basic_config

from app.models import TuItServiceBroker


def create_app():
    app = Flask(__name__)
    logger = basic_config()

    openbroker_bp = api.get_blueprint(TuItServiceBroker(), api.BrokerCredentials("", ""), logger)
    app.register_blueprint(openbroker_bp)

    return app
