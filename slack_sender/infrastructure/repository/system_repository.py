from datetime import datetime

from injector import inject

from slack_sender.infrastructure.configuration import Configuration
from slack_sender.infrastructure.model.system import System


class SystemRepository:
    @inject
    def __init__(self, config: Configuration):
        self._table = config.dynamodb.Table(config.system_table_name)
        self.system_id = config.system_id
        self.datetime_format = config.date_format

    def get(self):
        response = self._table.get_item(Key={
            System.SYSTEM_ID_NAME: self.system_id
        })
        return System(response["Item"], self.datetime_format)

    def update_last_startup(self):
        self._table.update_item(
            Key={
                System.SYSTEM_ID_NAME: self.system_id
            },
            UpdateExpression='SET {} = :val1'.format(System.LAST_STARTUP),
            ExpressionAttributeValues={
                ':val1': datetime.now().strftime(self.datetime_format)
            })
