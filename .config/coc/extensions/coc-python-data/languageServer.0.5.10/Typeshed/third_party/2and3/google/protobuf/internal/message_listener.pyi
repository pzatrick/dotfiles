class MessageListener(object):
    def Modified(self) -> None: ...

class NullMessageListener(MessageListener):
    def Modified(self) -> None: ...
