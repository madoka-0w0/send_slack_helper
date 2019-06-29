from injector import provider, singleton

from slack_sender.infrastructure.configuration import Configuration
from slack_sender.infrastructure.repository.system_repository import SystemRepository
import boto3

from slack_sender.infrastructure.repository.user_repository import UserRepository


@singleton
@provider
def provider_system_repository(configuration: Configuration) -> SystemRepository:
    dynamodb = boto3.resource('dynamodb')
    return SystemRepository(dynamodb.Table(configuration.system_table_name), configuration.system_id,
                            configuration.date_format)


@singleton
@provider
def provider_user_repository(configuration: Configuration) -> UserRepository:
    dynamodb = boto3.resource('dynamodb')
    return UserRepository(dynamodb.Table(configuration.user_table_name))
