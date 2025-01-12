import numpy as np
from numpy import array

from sudoku.board.cell import Cell
from sudoku.board.helpers.coordinates import Coordinates
from sudoku.config.constants import BOARD_INIT, BOARD_DIMENSION


class Board:
    """Keeps track of a Sudoku Board information:
     - values and markups of Cells by coordinates
    Can give some Statistics
    """

    def __init__(self) -> None:
        """Object Initializer."""
        self.grid = np.array(BOARD_INIT)
        self.make_empty_board()

    def make_empty_board(self) -> None:
        """Create all Board's Cells as empty Cells."""
        for line in range(0, BOARD_DIMENSION):
            for column in range(0, BOARD_DIMENSION):
                self.grid[line][column] = Cell(None, Coordinates((line + 1, column + 1)))

    @property
    def validity(self) -> bool:
        """Return True if grid is a valid Sudoku square, otherwise False."""
        return True

    @property
    def givens(self) -> int:
        """Returns the number of Given Cells in a Board"""
        count = 0
        for cell in self.grid.flatten():
            if cell.value.value is not None:
                count += 1
        return count

    @property
    def blanks(self) -> int:
        """Returns the number of Empty Cells in a Board"""
        count = 0
        for cell in self.grid.flatten():
            if cell.value.value is None:
                count += 1
        return count

    def how_many(self, value) -> int:
        """Returns the number of a Number Occurences"""
        count = 0
        for cell in self.grid.flatten():
            if cell.value.value == value:
                count += 1
        return count

    @property
    def line(self) -> str:
        """Return one line string reprezentation of the grid."""
        return ''.join([f'{cell()}' for cell in self.grid.flatten()])

    def __str__(self) -> str:
        return str(self.grid)

    def __call__(self, coordinates) -> array:
        return self.grid[coordinates.line - 1][coordinates.column - 1]

    def __enter__(self) -> "Board":
        return self

    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        pass
