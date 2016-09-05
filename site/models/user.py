# coding: utf-8
from peewee import CharField, IntegerField, BooleanField
from werkzeug.security import generate_password_hash, check_password_hash
from models.base import BaseModel, database
from models.user_ss_info import UserSSInfo
from models.user_total_traffic import UserTotalTraffic
from models.const.user_traffic import UserTrafficUpdateEvent
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
    @database.atomic()
    def create(cls, email, name, password, reg_ip='127.0.0.1', referer_id=0):
        u = cls(email=email, name=name, password=generate_password_hash(password), reg_ip=reg_ip, referer_id=referer_id)
        u.save()
        UserSSInfo.create(user_id=u.id)
        UserTotalTraffic.create(user_id=u.id, update_event=UserTrafficUpdateEvent.create_account)
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

    @property
    def total_traffic(self):
        return UserTotalTraffic.get(UserTotalTraffic.user_id == self.id).total_traffic

    def verify_password(self, password):
        return check_password_hash(self.password, password)
