from functools import singledispatchmethod

from icecream import ic

from sudoku.board.helpers.exceptions import InvalidLineException, InvalidColumnException
from sudoku.config.constants import ALL_POSSIBILITIES_SET


class Coordinates:
    """Keeps track of the coordinates in the Sudoku Grid:
     - line
     - column
    of a Sudoku Cell
    Both line and colum can have values from 1 to 9 (not 0 to 8)
    Can keep track of a LINE coordinate or a COLUMN coordinate
    Can give information about the BLOCK in which the Cell is contained
    Coordinates has a line and column properties wich has a bytearray as a placeholder
    Can be initialized with integers or a None
    Can be populated after initialization with a None from integers
    """

    @singledispatchmethod
    def __init__(self):
        """Initialize with Void."""

    @__init__.register(type(None))
    def _from_none(self, coordinates: type(None)):
        """Initialize with None."""
        self._line = bytearray()
        self._column = bytearray()

    @__init__.register(tuple)
    def _from_tuple(self, coordinates: tuple):
        """Initialize with tuple."""
        line, column = coordinates
        self._line = bytearray()
        self._column = bytearray()
        self.line_from_int(line)
        self.column_from_int(column)

    @property
    def line(self):
        """Return Line."""
        if len(self._line) == 0:
            return None
        else:
            return int.from_bytes(bytes(self._line), 'big', signed=False)

    @property
    def column(self):
        """return  Column"""
        if len(self._column) == 0:
            return None
        else:
            return int.from_bytes(bytes(self._column), 'big', signed=False)

    def line_from_int(self, line: int | None = None):
        """Fill The Line from Int."""
        try:
            Coordinates.check_line(line)
        except InvalidLineException:
            ic("Invalid line")
        else:
            self._line.extend(line.to_bytes(1, 'big', signed=False))

    def column_from_int(self, column: int = None):
        """Fill The Column from Int."""
        try:
            Coordinates.check_column(column)
        except InvalidColumnException:
            ic("Invalid column")
        else:
            self._column.extend(column.to_bytes(1, 'big', signed=False))

    @property
    def block_line_start(self):
        """Return Block Line start."""
        return ((self.line - 1) // 3) * 3

    @property
    def block_line_finish(self):
        """Return Block Line finish."""
        return self.block_line_start + 3

    @property
    def block_column_start(self):
        """Return Block Column start."""
        return ((self.column - 1) // 3) * 3

    @property
    def block_column_finish(self):
        """Return Block Column Finish """
        return self.block_column_start + 3

    @staticmethod
    def check_line(element):
        """Check the line for value."""
        if element not in ALL_POSSIBILITIES_SET:
            raise InvalidLineException()

    @staticmethod
    def check_column(element):
        """Check the column for value."""
        if element not in ALL_POSSIBILITIES_SET:
            raise InvalidColumnException()

    def __str__(self) -> str:
        line_str = '_' if self.line is None else self.line
        column_str = '_' if self.column is None else self.column
        return f"({line_str}:{column_str})"

    def __eq__(self, other) -> bool:
        return (self.line == other.line) and (self.column == other.column)
