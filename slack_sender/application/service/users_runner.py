import logging

from injector import inject

from slack_sender.application.service.user_runner import UserRunner
from slack_sender.infrastructure.repository.user_repository import UserRepository


class UsersRunner:
    @inject
    def __init__(self, user_repo: UserRepository,
                 user_runner: UserRunner):
        self.user_repo = user_repo
        self.user_runner = user_runner
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self):
        for user in self.user_repo.get_users():
            try:
                self.user_runner.run(user)

            except Exception as e:
                self.logger.error("user id: {}, exception: {}".format(user.id, e), exc_info=True)
