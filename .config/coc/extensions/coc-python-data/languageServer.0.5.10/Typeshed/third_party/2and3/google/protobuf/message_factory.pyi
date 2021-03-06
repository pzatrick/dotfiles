from typing import Any, Dict, Iterable, Optional, Type

from .message import Message
from .descriptor import Descriptor
from .descriptor_pool import DescriptorPool

class MessageFactory:
    pool = ...  # type: Any
    def __init__(self, pool: Optional[DescriptorPool] = ...) -> None: ...
    def GetPrototype(self, descriptor: Descriptor) -> Type[Message]: ...
    def GetMessages(self, files: Iterable[bytes]) -> Dict[bytes, Type[Message]]: ...

def GetMessages(file_protos: Iterable[bytes]) -> Dict[bytes, Type[Message]]: ...
