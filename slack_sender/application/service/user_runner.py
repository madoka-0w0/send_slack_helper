from abc import abstractmethod

from injector import inject

from slack_sender.application.model.slack_message import SlackMessage
from slack_sender.application.slack_message_creator import SlackMessageCreator
from slack_sender.application.service.slack_sender import SlackSender
from slack_sender.infrastructure.model.user import User
from slack_sender.infrastructure.repository.user_repository import UserRepository


class UserRunner:
    @inject
    def __init__(self,
                 message_creator: SlackMessageCreator,
                 user_repo: UserRepository,
                 slack_sender: SlackSender):
        self.message_creator = message_creator
        self.slack_sender = slack_sender
        self.user_repo = user_repo

    def run(self, user: User):
        message = self.message_creator.create(user)
        if self.need_send_slack(user, message):
            self.slack_sender.send(user.slack_url, message)
        self.change_need_send_slack_status(user, message)

    @abstractmethod
    def need_send_slack(self, user: User, message: SlackMessage):
        return user.need_send_slack and not message.is_empty()

    @abstractmethod
    def change_need_send_slack_status(self, user: User, message: SlackMessage):
        status = not user.need_send_slack
        self.user_repo.update_need_send_slack(user.id, status)
