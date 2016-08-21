# coding: utf-8
from flask import request
from views import main_bp
from lib.render import ok, error
from models.user import User


@main_bp.route('/auth/sign-up.json', methods=['POST'])
def sign_up():
    email = request.form.get('email').strip()
    name = request.form.get('name').strip()
    password = request.form.get('password').strip()
    User.create(email=email, name=name, password=password)
    return ok()


@main_bp.route('/auth/login.json', methods=['POST'])
def login():
    email = request.form.get('email').strip()
    u = User.get(email=email)
    if not u:
        return error('用户尚未register')
    password = request.form.get('password').strip()
    if not u.verify_password(password):
        return error('密码错误')
    return ok('登陆成功')
