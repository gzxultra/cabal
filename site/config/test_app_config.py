# coding: utf-8
import os


class Config(object):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a hard to guess key'
    USER_INIT_TOTAL_TRAFFIC = 1024 * 10 # MB
