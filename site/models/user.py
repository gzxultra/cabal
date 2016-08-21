# coding: utf-8
from base import BaseModel
from peewee import CharField
from werkzeug.security import generate_password_hash, check_password_hash


class User(BaseModel):
    email = CharField(unique=True)
    name = CharField(unique=True)
    password = CharField()

    class Meta:
        db_table = 'user'

    @classmethod
    def create(cls, email, name, password):
        u = cls(email=email, name=name, password=generate_password_hash(password))
        return u.save()

    @classmethod
    def get_user_by_email(cls, email):
        return User.select().where(email=email)

    def verify_password(self, password):
        return check_password_hash(self.password, password)
