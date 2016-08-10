# coding: utf-8
from . import cabal_bp
from lib.render import ok
from models.user import User
from models.base import database


@cabal_bp.route('/')
def index():
    return ok('yeah! its a new day!')