# coding: utf-8
import datetime
from peewee import Model, DateTimeField, DoesNotExist
from playhouse.db_url import connect
from config import AppConfig
# from app import login_manager

database = connect(AppConfig.DB_URL)


# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)


class BaseModel(Model):

    create_time = DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database

    @classmethod
    def get(cls, *query, **kwargs):
        try:
            return super(BaseModel, cls).get(*query, **kwargs)
        except DoesNotExist:
            return None

    def save(self, *args, **kwargs):
        if hasattr(self, 'update_time'):
            self.update_time = datetime.datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)
