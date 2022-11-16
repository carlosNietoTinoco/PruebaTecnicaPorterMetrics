from dataclasses import dataclass

from chalicelib.application.domain.user import User
from chalicelib.application.repository.user_repository import UserRepository, UserRepositoryFunctionsEnum


@dataclass
class UserService():

    repository: UserRepository
    
    def create_user(self, user: User) -> User:
        return self.repository[UserRepositoryFunctionsEnum.CREATE_USER](user)

    def get_user(self, username: str) -> User:
        return self.repository[UserRepositoryFunctionsEnum.GET_USER_BY_USERNAME](username)

    def get_all_users(self) -> list[User]:
        return self.repository[UserRepositoryFunctionsEnum.GET_ALL_USERS]()

    def update_user(self, user: User) -> User:
        return self.repository[UserRepositoryFunctionsEnum.UPDATE_USER](user)

    def delete_user(self, username: str) -> User:
        return self.repository[UserRepositoryFunctionsEnum.DELETE_USER](username)
    
