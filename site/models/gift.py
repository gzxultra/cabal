# coding: utf-8
import random
from decimal import Decimal
from peewee import IntegerField
from models.base import BaseModel, database
from models.user_total_traffic import UserTotalTraffic


class UserLoginGift(BaseModel):
    id = IntegerField(primary_key=True)
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
        traffic_info = UserTotalTraffic.get(user_id == user_id)
        traffic_info.update(total_traffic=(traffic_info.total_traffic+gift).quantize(Decimal('1.00')), update_event=1).save()
        return gift
