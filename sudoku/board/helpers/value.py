from functools import singledispatchmethod

from icecream import ic

from sudoku.board.helpers.exceptions import InvalidValueException
from sudoku.config.constants import ALL_POSSIBILITIES_SET


class Value:
    """Keeps track of the value of a Sudoku Cell.
    A Cell has a value property wich has a bytearray as a placeholder.
    It can be initialized with an integer or a string character or a None.
    It can be populated after initialization with a None from an integer or a string character.
    """
    @singledispatchmethod
    def __init__(self):
        """Initialize with Void."""

    @__init__.register(type(None))
    def _from_none(self, value: type(None)):
        """Initialize with None."""
        self._value = bytearray()

    @__init__.register(int)
    def _from_int(self, value: int):
        """Initialize with integer."""
        self._value = bytearray()
        self.from_int(value)

    @__init__.register(str)
    def _from_str(self, value: str):
        """Initialize with string."""
        self._value = bytearray()
        self.from_str(value)

    @property
    def value(self):
        """Getter Value property."""
        if len(self._value) == 0:
            return None
        else:
            return int.from_bytes(bytes(self._value), 'big', signed=False)

    def from_int(self, value: int):
        """Fill The Value from Int."""
        try:
            self.check(value)
        except InvalidValueException:
            ic("Invalid value")
        else:
            self._value.clear()
            self._value.extend(value.to_bytes(1, 'big', signed=False))

    def from_str(self, value: str):
        """Fill The Value from String."""
        try:
            self.check(int(value))
        except InvalidValueException:
            ic("Invalid value")
        else:
            self._value.clear()
            self._value.extend(int(value) .to_bytes(1, 'big', signed=False))

    def clear(self):
        """Clear Value."""
        self._value.clear()

    @staticmethod
    def check(value) -> bool:
        """Check Value."""
        if value not in ALL_POSSIBILITIES_SET:
            raise InvalidValueException()

    def __str__(self) -> str:
        if self.value is None:
            return f"{0}"
        else:
            return f"{self.value}"

    def __call__(self) -> int:
        if self.value is None:
            return 0
        else:
            return self.value

    def __eq__(self, other):
        return self.value == other.value