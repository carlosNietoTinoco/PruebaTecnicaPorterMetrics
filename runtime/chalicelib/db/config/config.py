import os

from enum import Enum, auto

class ConfigEnum(Enum):
    TABLE_NAME_IN_PYNAMO = auto()

def get_table_name_in_pynamo() -> str:
    return os.environ.get("TABLE_NAME_IN_PYNAMO", "test_user_model")


config: dict = {
    ConfigEnum.TABLE_NAME_IN_PYNAMO: get_table_name_in_pynamo()
}