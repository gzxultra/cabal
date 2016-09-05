# coding: utf-8
import sys
import os

sys.path.append(os.getcwd() + '/site')


def test_env():
    assert os.environ['CABAL_APP_CONFIG'] == 'config.test_app_config'
    assert os.environ['CABAL_DB_CONFIG'] == 'config.test_db_config'


def test_salts_are_random(user1, user2):
    assert user1.password != user2.password
