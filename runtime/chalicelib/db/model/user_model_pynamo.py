import os

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

from chalicelib.db.config.config import config, ConfigEnum

class UserModelPynamo(Model):
    class Meta:
        table_name = config[ConfigEnum.TABLE_NAME_IN_PYNAMO]
    username = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(range_key=True)
    