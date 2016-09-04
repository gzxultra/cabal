# coding: utf-8
from peewee import CharField, IntegerField, BooleanField
from werkzeug.security import generate_password_hash, check_password_hash
from models.base import BaseModel, database
from models.user_ss_info import UserSSInfo
from models.user_total_traffic import UserTotalTraffic
from flask_login import UserMixin


class User(UserMixin, BaseModel):
    id = IntegerField(primary_key=True)
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
    @database.atomic()
    def create(cls, email, name, password, reg_ip='127.0.0.1', referer_id=0):
        u = cls(email=email, name=name, password=generate_password_hash(password), reg_ip=reg_ip, referer_id=referer_id)
        u.save()
<<<<<<< da90bed9d999d2055b40eedc9f4e8bb700e63200
        UserSSInfo.create(u.id)
        UserTotalTraffic.create(user_id=u.id)
=======
        UserSSInfo.create(user_id=u.id)
>>>>>>> update ss info table
        return u

    @classmethod
    def get_user_by_email(cls, email):
        return User.get(cls.email == email)

    @property
    def port(self):
        return UserSSInfo.get(User.user_id == self.id).port

    @property
    def ss_password(self):
        return UserSSInfo.get(User.user_id == self.id).password

    def verify_password(self, password):
        return check_password_hash(self.password, password)
