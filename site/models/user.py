# coding: utf-8
from base import BaseModel
from peewee import CharField
from lib.encrypt import hash_password



class User(BaseModel):
    email = CharField(unique=True)
    name = CharField(unique=True)
    password = CharField()

    class Meta:
        db_table = 'user'

    @classmethod
    def create(cls, name, password):
        u = cls(name=name, password=hash_password(password))
        return u.save()

    def verify_password(self, email, password):
        return hash_password(password) == self.password

