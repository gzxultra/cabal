# coding: utf-8
from flask import request
from views import main_bp
from lib.render import ok, error
from lib.ip import get_ip_by_request
from models.user import User


@main_bp.route('/auth/sign-up.json', methods=['POST'])
def sign_up():
    email = request.form.get('email').strip()
    name = request.form.get('name').strip()
    password = request.form.get('password').strip()
    reg_ip = get_ip_by_request(request)
    User.create(email=email, name=name, password=password, reg_ip=reg_ip)
    return ok('sign up success')


@main_bp.route('/auth/login.json', methods=['POST'])
def login():
    email = request.form.get('email').strip()
    u = User.get(email=email)
    if not u:
        return error('no account found by the email')
    password = request.form.get('password').strip()
    if not u.verify_password(password):
        return error('wrong password')
    return ok('login success')
