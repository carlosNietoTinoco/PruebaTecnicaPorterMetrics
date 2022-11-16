import os

from chalicelib.application.domain.user import User

from chalicelib.db.mapper.user_pynamo_mapper import map_to_domain, map_to_entity
from chalicelib.db.model.user_model_pynamo import UserModelPynamo


UserModelPynamo.create_table(read_capacity_units=1, write_capacity_units=1)


def create_user(user: User) -> User:
    user_model: UserModelPynamo = map_to_entity(user)
    user_model.save()
    return user

def get_user_by_username(username: str) -> User:
    try:
        return map_to_domain(UserModelPynamo.get(username))
    except UserModelPynamo.DoesNotExist:
        return None

def get_all_users() -> list[User]:
    users = []
    for user in UserModelPynamo.scan():
        users.append(map_to_domain(user))
    return users

def update_user(user: User) -> User:
    user_model: UserModelPynamo = map_to_entity(user)
    user_model.save()
    return user

def delete_user(username: str) -> User:
    try:
        user_model = UserModelPynamo.get(username)
    except UserModelPynamo.DoesNotExist:
        return None
    user: User = map_to_domain(user_model)
    # TODO: error delete_user
    user_model.delete()
    return user

def get_functions_user_repository_pynamo() -> tuple[
    create_user, get_user_by_username, get_all_users, update_user, delete_user]:
    return create_user, get_user_by_username, get_all_users, update_user, delete_user
