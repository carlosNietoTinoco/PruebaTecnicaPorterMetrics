import json
from chalice import Blueprint

from chalicelib.blueprint.mapper.user_mapper import to_domain, domain_to_response, domain_list_to_response
from chalicelib.application.service.user_services import UserService
from chalicelib.dependencies.dependencies_config import get_user_service

user_api = Blueprint(__name__)

user_services: UserService = get_user_service()


@user_api.route('/users', methods=['POST'])
def create_user() -> json:
    # TODO: return code 201
    return domain_to_response(user_services.create_user(
        to_domain(user_api.current_request.json_body)))


@user_api.route('/users/{username}', methods=['GET'])
def get_user(username: str) -> json:
    return domain_to_response(user_services.get_user(username))


@user_api.route('/users', methods=['GET'])
def get_all_users() -> json:
    return domain_list_to_response(user_services.get_all_users())
    

@user_api.route('/users', methods=['PUT'])
def update_user() -> json:
    return domain_to_response(user_services.update_user(
        to_domain(user_api.current_request.json_body)))


@user_api.route('/users/{username}', methods=['DELETE'])
def delete_user(username: str) -> json:
    return domain_to_response(user_services.delete_user(username))