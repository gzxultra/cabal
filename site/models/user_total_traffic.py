# coding: utf-8
from decimal import Decimal
from peewee import IntegerField, DecimalField, SmallIntegerField
from models.base import BaseModel, database
from config import AppConfig


class UserTotalTraffic(BaseModel):
    user_id = IntegerField()
    total_traffic = DecimalField()
    update_event = SmallIntegerField()

    class Meta:
        db_table = 'user_total_traffic'

    @classmethod
    @database.atomic()
    def create(cls, user_id, update_event):
        total_traffic = Decimal(AppConfig.USER_INIT_TOTAL_TRAFFIC).quantize(Decimal('1.00'))
        print total_traffic
        user_traffic_info = cls(user_id=user_id, total_traffic=total_traffic, update_event=update_event)
        user_traffic_info.save()
        return user_traffic_info
