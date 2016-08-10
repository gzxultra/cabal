# coding: utf-8
import time
from flask import request
from . import cabal_bp
from lib.render import ok
from lib.encrypt import hash_password
from models.user import User
from models.base import database


@cabal_bp.route('/')
def index():
    return ok('yeah! its a new day!')


@cabal_bp.route('/register.json', methods=['POST'])
def register():
    name = request.form.get('name')
    password = request.form.get('password')
    User.create(name=name, password=hash_password(password))
    return ok()
