# coding: utf-8
from base import BaseModel
from peewee import CharField


class User(BaseModel):
    name = CharField(unique=True)
    password = CharField()

    class Meta:
        db_table = 'user'

    @classmethod
    def create(cls, name, password):
        u = cls(name=name, password=password)
        u.save()
        return u
