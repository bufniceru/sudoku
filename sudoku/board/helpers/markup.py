from sudoku.config.constants import ALL_POSSIBILITIES_SET


class Markup:
    """Keeps track of the markup of a Sudoku Cell
    A Markup contains all possible values that can be place in a Cell
    at a given time as the Solving process take place due to the Strategies
    """
    def __init__(self):
        """Object initializer."""
        self._value = set(ALL_POSSIBILITIES_SET)

    @property
    def value(self):
        """Getter Value property."""
        return self._value

    @value.setter
    def value(self, value):
        """Setter Value property."""
        self._value = value

    def discard(self, number):
        """Eliminated a number from Markup value."""
        self._value.discard(number)

    def discard_all(self):
        """Eliminated all numbers from Markup value."""
        self._value.clear()

    def reset(self):
        """Reset Markup to its initial value with all possible numbers."""
        self._value = set(ALL_POSSIBILITIES_SET)

    def __str__(self):
        return f"{self.value}"

    def __eq__(self, other):
        return self.value == other.value
