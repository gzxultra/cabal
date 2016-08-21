# coding: utf-8
from flask import request, render_template, url_for
from views import main_bp
from lib.render import ok, error
from models.user import User


@main_bp.route('/', methods=['GET'])
def index():
    return ok('Yeah, it\'s a god damn new day!')


# @main_bp.route("/all-links")
# def all_links():
#     links = []
#     for rule in app.url_map.iter_rules():
#         if len(rule.defaults) >= len(rule.arguments):
#             url = url_for(rule.endpoint, **(rule.defaults or {}))
#             links.append((url, rule.endpoint))
#     return render_template("show_links.html", links=links)
