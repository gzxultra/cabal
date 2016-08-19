# coding: utf-8
from flask import Blueprint


cabal = Blueprint(
    'cabal',
    __name__,
    template_folder='templates',
    static_folder='static')

from views import main  # noqa