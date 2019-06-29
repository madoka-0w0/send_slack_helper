from abc import ABC

from slack_sender.application.model.slack_message import SlackMessage
from slack_sender.infrastructure.model.user import User


class SlackMessageCreator(ABC):
    def create(cls, user: User) -> SlackMessage:
        pass
