# coding: utf-8
import sys
import os
import pytest

sys.path.append(os.getcwd() + '/site')
from models.user import User


@pytest.fixture(scope="module")
def user1():
    user1 = User.create(email='abc1@abc.com', name='cat', password='dog')
    yield user1


@pytest.fixture(scope="module")
def user2():
    user2 = User.create(email='abc2@abc.com', name='cat', password='dog')
    yield user2
