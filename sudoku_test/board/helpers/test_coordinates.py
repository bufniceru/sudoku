from sudoku.board.helpers.coordinates import Coordinates


class TestCoordinates:
    def test_coordinates_constructor_none(self):

        sut = Coordinates(None)

        assert hasattr(sut, 'line') is True
        assert hasattr(sut, 'column') is True

        assert sut.line is None
        assert sut.column is None

        assert f'{sut}' == '(_:_)'

    def test_coordinates_constructor_tuple_int_int(self):

        sut = Coordinates((3,6))

        assert hasattr(sut, 'line') is True
        assert hasattr(sut, 'column') is True

        assert sut.line == 3
        assert sut.column == 6

        assert f'{sut}' == '(3:6)'

    def test_coordinates_constructor_just_line(self):

        sut = Coordinates((3,None))

        assert hasattr(sut, 'line') is True
        assert hasattr(sut, 'column') is True

        assert sut.line == 3
        assert sut.column is None

        assert f'{sut}' == '(3:_)'

    def test_coordinates_constructor_just_column(self):

        sut = Coordinates((None,6))

        assert hasattr(sut, 'line') is True
        assert hasattr(sut, 'column') is True

        assert sut.line is None
        assert sut.column == 6

        assert f'{sut}' == '(_:6)'

    def test_coordinates_constructor_out_of_range_0_0(self):

        sut = Coordinates((0,0))

        assert hasattr(sut, 'line') is True
        assert hasattr(sut, 'column') is True

        assert sut.line is None
        assert sut.column is None

        assert f'{sut}' == '(_:_)'

    def test_coordinates_constructor_out_of_range_10_10(self):

        sut = Coordinates((10,10))

        assert hasattr(sut, 'line') is True
        assert hasattr(sut, 'column') is True

        assert sut.line is None
        assert sut.column is None

        assert f'{sut}' == '(_:_)'

    def test_coordinates_block_1_1(self):

        sut = Coordinates((1,1))

        assert sut.line == 1
        assert sut.column == 1

        assert sut.block_line_start == 0
        assert sut.block_line_finish == 3

        assert sut.block_column_start == 0
        assert sut.block_column_finish == 3

    def test_coordinates_block_1_3(self):

        sut = Coordinates((1,3))

        assert sut.line == 1
        assert sut.column == 3

        assert sut.block_line_start == 0
        assert sut.block_line_finish == 3

        assert sut.block_column_start == 0
        assert sut.block_column_finish == 3

    def test_coordinates_block_3_1(self):

        sut = Coordinates((3,1))

        assert sut.line == 3
        assert sut.column == 1

        assert sut.block_line_start == 0
        assert sut.block_line_finish == 3

        assert sut.block_column_start == 0
        assert sut.block_column_finish == 3

    def test_coordinates_block_3_3(self):

        sut = Coordinates((3,3))

        assert sut.line == 3
        assert sut.column == 3

        assert sut.block_line_start == 0
        assert sut.block_line_finish == 3

        assert sut.block_column_start == 0
        assert sut.block_column_finish == 3

    def test_coordinates_block_4_4(self):

        sut = Coordinates((4,4))

        assert sut.line == 4
        assert sut.column == 4

        assert sut.block_line_start == 3
        assert sut.block_line_finish == 6

        assert sut.block_column_start == 3
        assert sut.block_column_finish == 6

    def test_coordinates_block_4_6(self):

        sut = Coordinates((4,6))

        assert sut.line == 4
        assert sut.column == 6

        assert sut.block_line_start == 3
        assert sut.block_line_finish == 6

        assert sut.block_column_start == 3
        assert sut.block_column_finish == 6

    def test_coordinates_block_6_4(self):

        sut = Coordinates((6,4))

        assert sut.line == 6
        assert sut.column == 4

        assert sut.block_line_start == 3
        assert sut.block_line_finish == 6

        assert sut.block_column_start == 3
        assert sut.block_column_finish == 6

    def test_coordinates_block_6_6(self):

        sut = Coordinates((6,6))

        assert sut.line == 6
        assert sut.column == 6

        assert sut.block_line_start == 3
        assert sut.block_line_finish == 6

        assert sut.block_column_start == 3
        assert sut.block_column_finish == 6

    def test_coordinates_block_7_7(self):

        sut = Coordinates((7,7))

        assert sut.line == 7
        assert sut.column == 7

        assert sut.block_line_start == 6
        assert sut.block_line_finish == 9

        assert sut.block_column_start == 6
        assert sut.block_column_finish == 9

    def test_coordinates_block_7_9(self):

        sut = Coordinates((7,9))

        assert sut.line == 7
        assert sut.column == 9

        assert sut.block_line_start == 6
        assert sut.block_line_finish == 9

        assert sut.block_column_start == 6
        assert sut.block_column_finish == 9

    def test_coordinates_block_9_7(self):

        sut = Coordinates((9,7))

        assert sut.line == 9
        assert sut.column == 7

        assert sut.block_line_start == 6
        assert sut.block_line_finish == 9

        assert sut.block_column_start == 6
        assert sut.block_column_finish == 9

    def test_coordinates_block_9_9(self):

        sut = Coordinates((9,9))

        assert sut.line == 9
        assert sut.column == 9

        assert sut.block_line_start == 6
        assert sut.block_line_finish == 9

        assert sut.block_column_start == 6
        assert sut.block_column_finish == 9

    def test_coordinates_fill_none(self):

        sut = Coordinates(None)

        assert hasattr(sut, 'line') is True
        assert hasattr(sut, 'column') is True

        sut.line_from_int()
        sut.column_from_int()

        assert sut.line is None
        assert sut.column is None

        assert f'{sut}' == '(_:_)'

    def test_coordinates_fill(self):

        sut = Coordinates(None)

        assert hasattr(sut, 'line') is True
        assert hasattr(sut, 'column') is True

        sut.line_from_int(3)
        sut.column_from_int(6)

        assert sut.line == 3
        assert sut.column == 6

        assert f'{sut}' == '(3:6)'

    def test_coordonates_for_equality(self):

        sut_one = Coordinates((3, 7))
        sut_two = Coordinates((3, 7))

        assert (sut_one == sut_two) is True

    def test_coordinates_for_inequality(self):

        sut_one = Coordinates((5, 2))
        sut_two = Coordinates((8, 4))

        assert (sut_one == sut_two) is False