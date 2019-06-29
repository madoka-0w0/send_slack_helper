With `SystemRunner.run()`
After pre-processing, Users acquires all users in `UsersRunner`, and passes them to `UserRunner.run(user)`.
By default, `UserRunner` will attempt to send a message to the user's slack_url when the user's need_send_slack is true or the message is not empty.


## How To Use
* create implemented class

* create tables for System and User management in amazon dynamodb.

* bind configuration.

### Create Implemented Class
* slack_sender.application.slack_message_creator.SlackMessageCreator
```python
from slack_sender.application.slack_message_creator import SlackMessageCreator
from slack_sender.application.model.slack_message import SlackMessage 
from slack_sender.infrastructure.model.user import User

class TestMessage(SlackMessageCreator):
    def create(cls, user: User) -> SlackMessage:
        return SlackMessage(message="test")
```

### Create Tables In Amazon Dynamodb
#### Table Structure
##### System Table
* system_id # primary key
* last_startup # follow the date_format set in Configuration

##### User Table
* user_id # primary key
* need_send_slack
* slack_url
* channel # if you need

#### How To Use Dynamodb
Please refer to the following url.
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html

### Bind Configuration

bind Configuration instance to Configuration and SlackMessageCreator to class that you created extend.
```python
from injector import singleton, Injector
from slack_sender.application.service.system_runner import SystemRunner
from slack_sender.application.slack_message_creator import SlackMessageCreator
from slack_sender.infrastructure.configuration import Configuration

def configure(binder):
    binder.bind(Configuration,
                to=Configuration('system_table_name','user_table_name','system_id','date_format'),
                # date_format : for python. ex. '%Y%m%d_%H%M%S'
                scope=singleton # if you need
    )
    binder.bind(SlackMessageCreator,
                to=TestMessage)

if __name__ == '__main__':
    injector = Injector([configure])
    sys_runner = injector.get(SystemRunner)
    sys_runner.run()
```
or 
```python
from injector import singleton, Module, Injector
from slack_sender.application.service.system_runner import SystemRunner
from slack_sender.application.slack_message_creator import SlackMessageCreator
from slack_sender.infrastructure.configuration import Configuration

class BindModule(Module):
    def configure(self, binder):
        binder.bind(Configuration,
                    to=Configuration('system_table_name','user_table_name','system_id','date_format'),
                    scope=singleton# if you need
        )
        binder.bind(SlackMessageCreator,
                    to=TestMessage)
                    
if __name__ == '__main__':
    injector = Injector([BindModule()])
    sys_runner = injector.get(SystemRunner)
    sys_runner.run()
                 
```


## Class You Want To Inherit As Needed
* slack_sender.application.service.system_runner.SystemRunner
* slack_sender.application.service.users_runner.UsersRunner
* slack_sender.application.service.user_runner.UserRunner






