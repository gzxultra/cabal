# coding: utf-8
from flask import Flask
from config import AppConfig
from views import main_bp
from flask_login import LoginManager


app = Flask(__name__)
login_manager = LoginManager()
login_manager.login_view = 'views.main.login'

app.config.from_object(AppConfig)

login_manager.init_app(app)
# register_hooks(app)

app.register_blueprint(main_bp)
