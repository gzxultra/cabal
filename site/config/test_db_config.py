# coding: utf-8
import os


class Config(object):
    username = os.environ['USER']

    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_NAME = 'cabal_test_%s' % username
    DB_PORT = 3306

    DB_URL = 'mysql://%s@%s:%s/%s?charset=utf8mb4' % (DB_USER, DB_HOST, DB_PORT, DB_NAME)
#     DB_URL = 'mysql://%s:%s@%s:%s/%s?charset=utf8mb4' % (DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

