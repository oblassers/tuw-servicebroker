from flask import Flask
from openbrokerapi import api
from openbrokerapi.log_util import basic_config

from app.models import TuFilesServiceBroker, TuProCloudServiceBroker, TuHostServiceBroker


def create_app():
    app = Flask(__name__)
    logger = basic_config()

    openbroker_bp = api.get_blueprint([TuFilesServiceBroker(), TuProCloudServiceBroker(), TuHostServiceBroker()],
                                      api.BrokerCredentials("", ""), logger)
    app.register_blueprint(openbroker_bp)

    return app
