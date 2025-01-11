from sudoku.board.cell import Cell
from sudoku.board.helpers.coordinates import Coordinates
from sudoku.config.constants import ALL_POSSIBILITIES_SET, EMPTY_SET


class TestCell:
    def test_cell_constructor_void(self):

        sut = Cell()

        assert hasattr(sut, 'value') is True
        assert hasattr(sut, 'markup') is True
        assert hasattr(sut, 'coordinates') is True

        assert sut.value.value is None
        assert sut.value() == 0
        assert sut.markup.value == ALL_POSSIBILITIES_SET
        assert sut.coordinates.line is None
        assert sut.coordinates.column is None
        assert sut() == 0

    def test_cell_constructor(self):

        sut = Cell(5, Coordinates((3,6)))

        assert hasattr(sut, 'value') is True
        assert hasattr(sut, 'markup') is True
        assert hasattr(sut, 'coordinates') is True

        assert sut.value.value == 5
        assert sut.value() == 5
        assert sut.markup.value == EMPTY_SET
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6
        assert sut() == 5

    def test_cell_constructor_none_value(self):

        sut = Cell(None, Coordinates((3,6)))

        assert hasattr(sut, 'value') is True
        assert hasattr(sut, 'markup') is True
        assert hasattr(sut, 'coordinates') is True

        assert sut.value.value is None
        assert sut.value() == 0
        assert sut.markup.value == ALL_POSSIBILITIES_SET
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6
        assert sut() == 0

    def test_cell_constructor_zero_value(self):

        sut = Cell(0, Coordinates((3,6)))

        assert hasattr(sut, 'value') is True
        assert hasattr(sut, 'markup') is True
        assert hasattr(sut, 'coordinates') is True

        assert sut.value.value is None
        assert sut.value() == 0
        assert sut.markup.value == ALL_POSSIBILITIES_SET
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6
        assert sut() == 0

    def test_cell_constructor_ten_value(self):

        sut = Cell(10, Coordinates((3,6)))

        assert hasattr(sut, 'value') is True
        assert hasattr(sut, 'markup') is True
        assert hasattr(sut, 'coordinates') is True

        assert sut.value.value is None
        assert sut.value() == 0
        assert sut.markup.value == ALL_POSSIBILITIES_SET
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6
        assert sut() == 0

    def test_cell_clear_cell(self):

        sut = Cell(7, Coordinates((3,6)))

        assert hasattr(sut, 'value') is True
        assert hasattr(sut, 'markup') is True
        assert hasattr(sut, 'coordinates') is True

        sut.clear_cell()

        assert sut.value.value is None
        assert sut.value() == 0
        assert sut.markup.value == ALL_POSSIBILITIES_SET
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6
        assert sut() == 0

    def test_cell_markup_discard(self):

        sut = Cell(0, Coordinates((3,6)))

        assert hasattr(sut, 'value') is True
        assert hasattr(sut, 'markup') is True
        assert hasattr(sut, 'coordinates') is True

        sut.markup.discard(7)

        assert sut.value.value is None
        assert sut.value() == 0
        set_to_compare = set(ALL_POSSIBILITIES_SET)
        set_to_compare.remove(7)
        assert sut.markup.value == set_to_compare
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6
        assert sut() == 0

        sut.markup.discard(3)

        assert sut.value.value is None
        assert sut.value() == 0
        set_to_compare.remove(3)
        assert sut.markup.value == set_to_compare
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6
        assert sut() == 0

        sut.markup.discard(9)

        assert sut.value.value is None
        assert sut.value() == 0
        set_to_compare.remove(9)
        assert sut.markup.value == set_to_compare
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6
        assert sut() == 0

        sut.markup.discard(5)

        assert sut.value.value is None
        assert sut.value() == 0
        set_to_compare.remove(5)
        assert sut.markup.value == set_to_compare
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6
        assert sut() == 0

        sut.markup.discard(2)

        assert sut.value.value is None
        assert sut.value() == 0
        set_to_compare.remove(2)
        assert sut.markup.value == set_to_compare
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6
        assert sut() == 0

        sut.markup.discard(8)

        assert sut.value.value is None
        assert sut.value() == 0
        set_to_compare.remove(8)
        assert sut.markup.value == set_to_compare
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6
        assert sut() == 0

        sut.markup.discard(1)

        assert sut.value.value is None
        assert sut.value() == 0
        set_to_compare.remove(1)
        assert sut.markup.value == set_to_compare
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6
        assert sut() == 0

        sut.markup.discard(4)

        assert sut.value.value is None
        assert sut.value() == 0
        set_to_compare.remove(4)
        assert sut.markup.value == set_to_compare
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6
        assert sut() == 0

        sut.markup.discard(6)

        assert sut.value.value is None
        assert sut.value() == 0
        set_to_compare.remove(6)
        assert sut.markup.value == set()
        assert sut.coordinates.line == 3
        assert sut.coordinates.column == 6
        assert sut() == 0

    def test_cell_fill_value_7(self):

        sut = Cell()

        assert hasattr(sut, 'value') is True
        assert hasattr(sut, 'markup') is True
        assert hasattr(sut, 'coordinates') is True

        assert sut.value.value is None
        assert sut.value() == 0
        assert sut.markup.value == ALL_POSSIBILITIES_SET
        assert sut.coordinates.line is None
        assert sut.coordinates.column is None
        assert sut() == 0

        sut.value = 7

        assert hasattr(sut, 'value') is True
        assert hasattr(sut, 'markup') is True
        assert hasattr(sut, 'coordinates') is True

        assert sut.value.value == 7
        assert sut.value() == 7
        assert sut.markup.value == EMPTY_SET
        assert sut.coordinates.line is None
        assert sut.coordinates.column is None
        assert sut() == 7

    def test_cell_for_equality_all(self):

        sut_one = Cell(3, Coordinates((7, 2)))
        sut_two = Cell(3, Coordinates((7, 2)))

        assert (sut_one == sut_two) is True

    def test_cell_for_inequality_all(self):

        sut_one = Cell(3, Coordinates((7, 2)))
        sut_two = Cell(7, Coordinates((4, 5)))

        assert (sut_one == sut_two) is False

    def test_cell_for_inequality_values(self):

        sut_one = Cell(3, Coordinates((7, 2)))
        sut_two = Cell(7, Coordinates((7, 2)))

        assert (sut_one == sut_two) is False

    def test_cell_for_inequality_oordinates(self):

        sut_one = Cell(3, Coordinates((7, 2)))
        sut_two = Cell(3, Coordinates((4, 5)))

        assert (sut_one == sut_two) is False