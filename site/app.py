# coding: utf-8
from flask import Flask
from flask_login import LoginManager

from config import AppConfig
from views import main_bp
from models.user import User


app = Flask(__name__)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main_bp.index'

app.config.from_object(AppConfig)

login_manager.init_app(app)
# register_hooks(app)

app.register_blueprint(main_bp)


@login_manager.user_loader
def load_user(user_id):
    return User.get(User.id == int(user_id))
