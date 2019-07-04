import unittest
from unittest.mock import Mock

from injector import singleton, Injector

from slack_sender.application.service.system_runner import SystemRunner
from slack_sender.infrastructure.configuration import Configuration
from slack_sender.infrastructure.model.user import User
from slack_sender.infrastructure.repository.system_repository import SystemRepository
from slack_sender.infrastructure.repository.user_repository import UserRepository


def config(binder):
    binder.bind(Configuration, to=Configuration("system_table_name", "user_table_name", 3, "%Y%M%d %H%M%S"),
                scope=singleton)
    user_repo = Mock()
    user_repo.get_users.return_value = [User({User.USERID_NAME: 1,
                                              User.NEED_SEND_SLACK_NAME: True,
                                              User.slack_url: "",
                                              })]
    binder.bind(UserRepository, to=user_repo, scope=singleton)
    binder.bind(SystemRepository, to=Mock(), scope=singleton)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        injector = Injector([config])
        system_runner = injector.get(SystemRunner)
        system_runner.run()


if __name__ == '__main__':
    unittest.main()
