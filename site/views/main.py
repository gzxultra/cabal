# coding: utf-8
from flask import request
from views import cabal
from lib.render import ok, error
from models.user import User


@cabal.route('/')
def index():
    return ok('yeah! its a new day!')


@cabal.route('/account/register.json', methods=['POST'])
def register():
    email = request.form.get('name').strip()
    name = request.form.get('name').strip()
    password = request.form.get('password').strip()
    User.create(email=email, name=name, password=password)
    return ok()


@cabal.route('/account/login.json', methods=['POST'])
def login():
    email = request.form.get('email').strip()
    u = User.get(email=email)
    if not u:
        return error('用户尚未')
    password = request.form.get('password').strip()
    if not u.verfiy_password(password):
        return error('密码错误')
    return ok('登陆成功')
