import boto3


class Configuration:
    def __init__(self, system_table_name, user_table_name, system_id, date_format):
        self.system_table_name = system_table_name
        self.user_table_name = user_table_name
        self.system_id = system_id
        self.date_format = date_format
        self.dynamodb = boto3.resource('dynamodb')

