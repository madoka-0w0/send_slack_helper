from datetime import datetime


class System(object):
    SYSTEM_ID_NAME = "system_id"
    LAST_STARTUP = "last_startup"

    def __init__(self, item: dict, datetime_format):
        self._item = item
        self.datetime_format = datetime_format

    @property
    def last_startup(self):
        return datetime.strptime(self._item.get(self.LAST_STARTUP), self.datetime_format)
