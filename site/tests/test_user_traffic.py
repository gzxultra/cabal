# coding: utf-8
import sys
import os
from models.gift import UserLoginGift

sys.path.append(os.getcwd() + '/site')

from config import AppConfig


def test_user_with_initial_traffic(user1):
    assert user1.total_traffic == AppConfig.USER_INIT_TOTAL_TRAFFIC


def test_user_login_gift(user1):
    user_total_traffic = user1.total_traffic
    gift = UserLoginGift.create(user_id=user1.id)
    assert user_total_traffic + gift.login_gift == user1.total_traffic
