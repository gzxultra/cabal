# coding: utf-8
from flask import Blueprint
from lib.render import error


main_bp = Blueprint('main_bp', __name__)


@main_bp.app_errorhandler(404)
def page_note_found(e):
    return error('page not found', status_code=404), 404

@main_bp.app_errorhandler(500)
def internal_server_erorr(e):
    return error('internal server error', status_code=500), 500


from . import auth, main
