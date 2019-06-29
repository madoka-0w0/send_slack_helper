class User(object):
    USERID_NAME = "userid"
    NEED_SEND_SLACK_NAME = "need_send_slack"
    SLACK_URL_NAME = "slack_url"
    CHANNEL_NAME = "channel"

    def __init__(self, item: dict):
        self._item = item

    @property
    def id(self):
        return self._item[self.USERID_NAME]

    @property
    def need_send_slack(self):
        return self._item[self.NEED_SEND_SLACK_NAME]

    @property
    def slack_url(self):
        return self._item[self.SLACK_URL_NAME]

    @property
    def channel(self):
        return self._item.get(self.CHANNEL_NAME)
