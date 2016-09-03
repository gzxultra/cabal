# coding: utf-8
import sys
import os
import pytest

sys.path.append(os.getcwd() +'/site')

from models.user import User


def test_env():
    assert os.environ['CABAL_APP_CONFIG'] == 'config.test_app_config'
    assert os.environ['CABAL_DB_CONFIG'] == 'config.test_db_config'

def test_salts_are_random():
    u1 = User.create(email='abc1@abc.com', name='cat', password='dog')
    u2 = User.create(email='abc2@abc.com', name='cat', password='dog')
    assert u1.password != u2.password
