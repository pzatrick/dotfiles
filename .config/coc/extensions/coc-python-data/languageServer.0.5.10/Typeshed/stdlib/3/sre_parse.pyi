# Source: https://github.com/python/cpython/blob/master/Lib/sre_parse.py

from typing import (
    Any, Dict, FrozenSet, Iterable, List, Match,
    Optional, Pattern as _Pattern, Tuple, Union
)
from sre_constants import _NamedIntConstant as NIC, error as _Error

SPECIAL_CHARS = ...  # type: str
REPEAT_CHARS = ...  # type: str
DIGITS = ...  # type: FrozenSet[str]
OCTDIGITS = ...  # type: FrozenSet[str]
HEXDIGITS = ...  # type: FrozenSet[str]
ASCIILETTERS = ...  # type: FrozenSet[str]
WHITESPACE = ...  # type: FrozenSet[str]
ESCAPES = ...  # type: Dict[str, Tuple[NIC, int]]
CATEGORIES = ...  # type: Dict[str, Union[Tuple[NIC, NIC], Tuple[NIC, List[Tuple[NIC, NIC]]]]]
FLAGS = ...  # type: Dict[str, int]
GLOBAL_FLAGS = ...  # type: int

class Verbose(Exception): ...

class Pattern:
    flags = ...  # type: int
    groupdict = ...  # type: Dict[str, int]
    groupwidths = ...  # type: List[Optional[int]]
    lookbehindgroups = ...  # type: Optional[int]
    def __init__(self) -> None: ...
    @property
    def groups(self) -> int: ...
    def opengroup(self, name: str = ...) -> int: ...
    def closegroup(self, gid: int, p: SubPattern) -> None: ...
    def checkgroup(self, gid: int) -> bool: ...
    def checklookbehindgroup(self, gid: int, source: Tokenizer) -> None: ...


_OpSubpatternType = Tuple[Optional[int], int, int, SubPattern]
_OpGroupRefExistsType = Tuple[int, SubPattern, SubPattern]
_OpInType = List[Tuple[NIC, int]]
_OpBranchType = Tuple[None, List[SubPattern]]
_AvType = Union[_OpInType, _OpBranchType, Iterable[SubPattern], _OpGroupRefExistsType, _OpSubpatternType]
_CodeType = Tuple[NIC, _AvType]


class SubPattern:
    pattern = ...  # type: Pattern
    data = ...  # type: List[_CodeType]
    width = ...  # type: Optional[int]
    def __init__(self, pattern: Pattern, data: List[_CodeType] = ...) -> None: ...
    def dump(self, level: int = ...) -> None: ...
    def __len__(self) -> int: ...
    def __delitem__(self, index: Union[int, slice]) -> None: ...
    def __getitem__(self, index: Union[int, slice]) -> Union[SubPattern, _CodeType]: ...
    def __setitem__(self, index: Union[int, slice], code: _CodeType) -> None: ...
    def insert(self, index: int, code: _CodeType) -> None: ...
    def append(self, code: _CodeType) -> None: ...
    def getwidth(self) -> int: ...


class Tokenizer:
    istext = ...  # type: bool
    string = ...  # type: Any
    decoded_string = ...  # type: str
    index = ...  # type: int
    next = ...  # type: Optional[str]
    def __init__(self, string: Any) -> None: ...
    def match(self, char: str) -> bool: ...
    def get(self) -> Optional[str]: ...
    def getwhile(self, n: int, charset: Iterable[str]) -> str: ...
    def getuntil(self, terminator: str) -> str: ...
    @property
    def pos(self) -> int: ...
    def tell(self) -> int: ...
    def seek(self, index: int) -> None: ...
    def error(self, msg: str, offset: int = ...) -> _Error: ...

def fix_flags(src: Union[str, bytes], flag: int) -> int: ...
def parse(str: str, flags: int = ..., pattern: Pattern = ...) -> SubPattern: ...
_TemplateType = Tuple[List[Tuple[int, int]], List[str]]
def parse_template(source: str, pattern: _Pattern) -> _TemplateType: ...
def expand_template(template: _TemplateType, match: Match) -> str: ...
