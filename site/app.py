# coding: utf-8
from flask import Flask
from config.sample_app_config import SampleAppConfig
from views import cabal
# from flask_login import LoginManager


app = Flask(__name__)
# login_manager = LoginManager()
# login_manager.login_view = 'views.main.login'

app.config.from_object(SampleAppConfig)

# login_manager.init_app(app)
# register_hooks(app)
app.register_blueprint(cabal, url_prefix='/cabal')
