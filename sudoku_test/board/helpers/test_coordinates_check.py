import pytest

from sudoku.board.helpers.coordinates import Coordinates
from sudoku.board.helpers.exceptions import InvalidLineException, InvalidColumnException


class TestCoordinatesCheck:
    def test_coordinates_constructor_check_inside(self):

        Coordinates.check_line(5)
        Coordinates.check_column(5)

    def test_coordinates_constructor_check_outside_low(self):

        with pytest.raises(InvalidLineException):
            Coordinates.check_line(0)
        with pytest.raises(InvalidColumnException):
            Coordinates.check_column(0)

    def test_coordinates_constructor_check_outside_high(self):

        with pytest.raises(InvalidLineException):
            Coordinates.check_line(10)
        with pytest.raises(InvalidColumnException):
            Coordinates.check_column(10)