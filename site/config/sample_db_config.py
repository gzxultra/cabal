# coding: utf-8


class Config(object):
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_NAME = 'cabal'
    DB_PORT = 3306

    DB_URL = 'mysql://%s@%s:%s/%s?charset=utf8mb4' % (DB_USER, DB_HOST, DB_PORT, DB_NAME)
