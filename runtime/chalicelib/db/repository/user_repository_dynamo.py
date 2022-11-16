import os
import boto3

from chalicelib.application.domain.user import User
from chalicelib.application.repository.user_repository import UserRepository

dynamodb = boto3.resource('dynamodb')
dynamodb_table = dynamodb.Table(os.environ.get('APP_TABLE_NAME', ''))

class UserRepositoryDynamo():
    
    def create_user(self, user: User) -> User:
        request: dict[str, str] = user.__dict__
        item: dict[str, str] = {
            'PK': 'User#%s' % request['username'],
            'SK': 'Profile#%s' % request['username'],
        }
        item.update(request)
        dynamodb_table.put_item(Item=item)
        return user

    def get_user_by_username(self, username: str) -> User:
        key = {
        'PK': 'User#%s' % username,
        'SK': 'Profile#%s' % username,
        }
        item = dynamodb_table.get_item(Key=key)['Item']
        del item['PK']
        del item['SK']
        
        return item

    def get_all_users(self) -> list[User]:
        """get all users."""

    def update_user(self, user: User) -> User:
        return create_user(user)

    def delete_user(self, user: User) -> User:
        """delete a user."""
