# coding: utf-8
import random
import string
import socket
from peewee import CharField, IntegerField
from models.base import BaseModel


def _find_an_available_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    addr, port = s.getsockname()
    s.close()
    return port


class PortRunsOutException(Exception):
    pass


class UserSSInfo(BaseModel):
    user_id = IntegerField()
    port = IntegerField()
    password = CharField()

    class Meta:
        db_table = 'user_ss_info'

    @classmethod
    def create(cls, user_id):
        # find an available port
        port = _find_an_available_port()
        if not port:
            raise PortRunsOutException
        # generate random password
        password = ''.join([random.choice(string.ascii_letters+string.digits) for i in range(8)])

        # create record
        info = UserSSInfo(user_id=user_id, port=port, password=password)
        info.save()
        return info
