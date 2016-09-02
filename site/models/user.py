# coding: utf-8
from peewee import CharField, IntegerField, BooleanField
from werkzeug.security import generate_password_hash, check_password_hash
from models.base import BaseModel
from flask_login import UserMixin


class User(UserMixin, BaseModel):
    email = CharField(unique=True)
    name = CharField()
    password = CharField()
    is_admin = BooleanField(default=False)
    is_email_verify = BooleanField(default=False)
    reg_ip = CharField(default='127.0.0.1')
    referer_id = IntegerField(default=0)

    class Meta:
        db_table = 'user'

    @classmethod
    def create(cls, email, name, password, reg_ip='127.0.0.1', referer_id=0):
        u = cls(email=email, name=name, password=generate_password_hash(password), reg_ip=reg_ip, referer_id=referer_id)
        return u.save()

    @classmethod
    def get_user_by_email(cls, email):
        return User.select().where(email=email)

    def verify_password(self, password):
        return check_password_hash(self.password, password)
