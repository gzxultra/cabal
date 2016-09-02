# coding: utf-8
from flask import request, flash
from views import main_bp
from lib.render import ok, error
from lib.ip import get_ip_by_request
from models.user import User
from flask_login import login_user, login_required, logout_user


@main_bp.route('/auth/sign-up.json', methods=['POST'])
def sign_up():
    email = request.form.get('email').strip()
    name = request.form.get('name').strip()
    password = request.form.get('password').strip()
    reg_ip = get_ip_by_request(request)
    User.create(email=email, name=name, password=password, reg_ip=reg_ip)
    return ok('sign up successfully')


@main_bp.route('/auth/login.json', methods=['POST'])
def login():
    email = request.form.get('email').strip()
    u = User.get(email=email)
    if not u:
        return error('no account found by the email')
    password = request.form.get('password').strip()
    if not u.verify_password(password):
        return error('wrong password')

    login_user(u)
    return ok('login successfully')


@main_bp.route('/auth/logout.json', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logout.')
    return ok('logout successfully')
