# coding: utf-8
from decimal import Decimal
from peewee import IntegerField
from models.base import BaseModel, database


class UserTotalTraffic(BaseModel):
    id = IntegerField(primary_key=True)
    user_id = IntegerField()
    total_traffic = Decimal(15, 2)
    update_event = 0

    class Meta:
        db_table = 'user_total_traffic'

    @classmethod
    @database.atomic()
    def create(cls, user_id, update_event):
        total_traffic = Decimal(1024).quantize(Decimal('1.00'))
        user_traffic_info = cls(user_id=user_id, total_traffic=total_traffic, update_event=update_event)
        user_traffic_info.save()
        return user_traffic_info
