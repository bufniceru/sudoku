from icecream import ic

from sudoku.board.helpers.coordinates import Coordinates
from sudoku.board.helpers.exceptions import InvalidValueException
from sudoku.board.helpers.markup import Markup
from sudoku.board.helpers.value import Value


class Cell:
    """Keeps track of Sudoku CELL information:
     - value
     - markup
     - coordinates
    Can keep track of a LINE or a COLUMN coordinate
    Can give information about the BLOCK in which the Cell is contained
    """
    def __init__(self, value=None, coordinates=None) -> None:
        if value is None:
            self._value = Value(None)
            self._markup = Markup()
        else:
            try:
                self._value = Value(value)
            except InvalidValueException:
                ic("Invalid value")
                self._value = Value(None)
                self._markup = Markup()
            else:
                self._markup = Markup()
                self._markup.discard_all()
        if coordinates is None:
            self._coordinates = Coordinates(None)
        else:
            self._coordinates = Coordinates((coordinates.line, coordinates.column))

    @property
    def value(self) -> Value:
        """Value Getter Property."""
        return self._value

    @value.setter
    def value(self, value) -> None:
        """Value Setter Property."""
        self._value.from_int(value)
        self._markup.discard_all()

    @property
    def markup(self) -> Markup:
        """Markup Getter Property."""
        return self._markup

    @markup.setter
    def markup(self, value) -> None:
        """Markup Setter Property."""
        self._markup = value

    @property
    def coordinates(self) -> Coordinates:
        """Coordinates Getter Property."""
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value) -> None:
        """Coordinates Setter Property."""
        self._coordinates = value

    def clear_cell(self) -> None:
        """Clear Cell"""
        self._value = Value(None)
        self._markup.reset()

    def __str__(self) -> str:
        return f"C[{self.coordinates.line},{self.coordinates.column}]({self.value})"

    def __repr__(self) -> str:
        return f"{self.value}" if self.value is not None else f"0"

    def __call__(self) -> int:
        return self.value()

    def __eq__(self, other) -> bool:
        return (self.value == other.value) and (self.coordinates == other.coordinates)
