# coding: utf-8
from flask_login import login_required
from views import main_bp
from lib.render import ok


@main_bp.route('/', methods=['GET'])
def index():
    return ok('Yeah, it\'s a god damn new day!')


@main_bp.route('/secret/', methods=['GET'])
@login_required
def secret():
    return ok('share secect with authorized people')
