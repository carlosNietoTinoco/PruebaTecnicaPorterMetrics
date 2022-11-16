from chalicelib.application.domain.user import User
from chalicelib.db.model.user_model_pynamo import UserModelPynamo


def map_to_entity(user: User) -> UserModelPynamo:
    return UserModelPynamo(user.username, user.name)

def map_to_domain(user: UserModelPynamo) -> User:
    return User(user.username, user.name)
