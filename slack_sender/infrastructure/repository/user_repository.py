from injector import inject

from slack_sender.infrastructure.configuration import Configuration
from slack_sender.infrastructure.model.user import User


class UserRepository:
    @inject
    def __init__(self, config: Configuration):
        self._table = config.dynamodb.Table(config.user_table_name)

    def get_users(self):
        response = self._table.scan()
        return [User(user) for user in response.get('Items', [])]

    def get_user(self, user_id: int):
        response = self._table.get_item(Key={
            User.USERID_NAME: user_id
        })
        return User(response["Item"])

    def update_need_send_slack(self, userid, status=None):
        status = True if status is None else status
        self._table.update_item(
            Key={
                User.USERID_NAME: userid
            },
            UpdateExpression='SET {} = :val1'.format(User.NEED_SEND_SLACK_NAME),
            ExpressionAttributeValues={
                ':val1': status
            })
