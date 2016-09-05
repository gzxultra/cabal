# coding: utf-8
import random
from decimal import Decimal
from peewee import IntegerField
from models.base import BaseModel, database
from models.user_total_traffic import UserTotalTraffic
from models.const.user_traffic import UserTrafficUpdateEvent


class UserLoginGift(BaseModel):
    user_id = IntegerField()
    login_gift = IntegerField()

    class Meta:
        db_table = 'user_login_gift'

    @classmethod
    @database.atomic()
    def create(cls, user_id):
        random_gift = random.randrange(50, 200)
        gift = cls(user_id=user_id, login_gift=random_gift)
        gift.save()
        traffic_info = UserTotalTraffic.get(UserTotalTraffic.user_id == user_id)
        update = traffic_info.update(total_traffic=(traffic_info.total_traffic+gift.login_gift).quantize(Decimal('1.00')),
            update_event=UserTrafficUpdateEvent.login_gift)
        update.execute()
        return gift

    @classmethod
    def get_user_gifted_history(cls, user_id):
        return [(i.login_gift, i.create_time) for i in cls.select().where(cls.user_id == user_id)]
