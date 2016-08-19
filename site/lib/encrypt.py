# coding: utf-8
from hashlib import sha256


def hash_password(id, password):
    return sha256("%s%s" % (password, id)).digest()
