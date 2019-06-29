from datetime import datetime

from slack_sender.infrastructure.model.system import System


class SystemRepository:
    def __init__(self, table, system_id, datetime_format):
        self._table = table
        self.system_id = system_id
        self.datetime_format = datetime_format

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
