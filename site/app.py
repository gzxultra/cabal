# coding: utf-8
import sys
from flask import Flask
from config import AppConfig
from views import cabal_bp
from models.base import database


app = Flask(__name__)
app.config.from_object(AppConfig)


def register_hooks(app):
    @app.before_request
    def _before_request():
        database.connect()

    @app.teardown_request
    def _teardown_request(exception):
        sys.stdout.flush()
        database.close()


register_hooks(app)
app.register_blueprint(cabal_bp, url_prefix='/cabal')