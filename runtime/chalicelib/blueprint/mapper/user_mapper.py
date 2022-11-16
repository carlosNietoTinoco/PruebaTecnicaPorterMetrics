import json

from chalicelib.application.domain.user import User

def to_domain(dict_: dict[str, str]) -> User:
    element = dict_.values()
    return User(list(element)[0], list(element)[1])


def domain_to_response(user: User) -> json:
    try:
        return json.dumps(user.__dict__)
    except AttributeError:
        return {}


def domain_list_to_response(users: list[User]) -> json:
    dictionary_with_all_users = {}
    for user in users:
        dictionary_with_all_users.update(user.__dict__)
    return json.dumps(dictionary_with_all_users)
