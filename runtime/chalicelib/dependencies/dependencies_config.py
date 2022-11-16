from chalicelib.application.repository.user_repository import UserRepository, build_user_repository
from chalicelib.application.service.user_services import UserService
from chalicelib.db.repository.user_repository_pynamo import get_functions_user_repository_pynamo

def get_user_service() -> UserService:
    repository: UserRepository = build_user_repository(
        get_functions_user_repository_pynamo())
    user_service: UserService = UserService(repository)
    return user_service

