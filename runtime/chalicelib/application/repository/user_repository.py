from enum import Enum, auto
from typing import Callable

from chalicelib.application.domain.user import User

FunctionCreateUser = Callable[[User], User], 
FunctionGetUserByUsername = Callable[[str], User], 
FunctionGetAllUsers = Callable[[], list[User]], 
FunctionUpdateUser = Callable[[User], User], 
FunctionDeleteUser = Callable[[str], User]

class UserRepositoryFunctionsEnum(Enum):
    CREATE_USER = auto()
    GET_USER_BY_USERNAME = auto()
    GET_ALL_USERS = auto()
    UPDATE_USER = auto()
    DELETE_USER = auto()

UserRepository: dict = {
    UserRepositoryFunctionsEnum.CREATE_USER: FunctionCreateUser,
    UserRepositoryFunctionsEnum.GET_USER_BY_USERNAME: FunctionGetUserByUsername,
    UserRepositoryFunctionsEnum.GET_ALL_USERS: FunctionGetAllUsers,
    UserRepositoryFunctionsEnum.UPDATE_USER: FunctionUpdateUser,
    UserRepositoryFunctionsEnum.DELETE_USER: FunctionDeleteUser
}

def build_user_repository(functions: tuple[
    FunctionCreateUser, FunctionGetUserByUsername, 
    FunctionGetAllUsers, FunctionUpdateUser, FunctionDeleteUser]) -> UserRepository:

        return {
            UserRepositoryFunctionsEnum.CREATE_USER: functions[0],
            UserRepositoryFunctionsEnum.GET_USER_BY_USERNAME: functions[1],
            UserRepositoryFunctionsEnum.GET_ALL_USERS: functions[2],
            UserRepositoryFunctionsEnum.UPDATE_USER: functions[3],
            UserRepositoryFunctionsEnum.DELETE_USER: functions[4]
        }