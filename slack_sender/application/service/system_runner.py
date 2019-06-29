from abc import abstractmethod

from injector import inject

from slack_sender.application.service.users_runner import UsersRunner
from slack_sender.infrastructure.repository.system_repository import SystemRepository


class SystemRunner:
    @inject
    def __init__(self, system_repo: SystemRepository, runner: UsersRunner):
        self.system_table = system_repo
        self.runner = runner

    def run(self):
        self.before_action()

        self.runner.run()

        self.after_action()

        self.system_table.update_last_startup()

    @abstractmethod
    def before_action(self):
        pass

    @abstractmethod
    def after_action(self):
        pass
