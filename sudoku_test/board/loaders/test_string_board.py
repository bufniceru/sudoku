from sudoku.board.cell import Cell
from sudoku.board.helpers.coordinates import Coordinates
from sudoku.board.loaders.string_board import StringBoard


class TestStringBoard:
    def test_string_board_indexes(self):

        assert StringBoard.index(0, 0) == 0
        assert StringBoard.index(0, 1) == 1
        assert StringBoard.index(0, 2) == 2
        assert StringBoard.index(0, 3) == 3
        assert StringBoard.index(0, 4) == 4
        assert StringBoard.index(0, 5) == 5
        assert StringBoard.index(0, 6) == 6
        assert StringBoard.index(0, 7) == 7
        assert StringBoard.index(0, 8) == 8

        assert StringBoard.index(1, 0) == 9
        assert StringBoard.index(1, 1) == 10
        assert StringBoard.index(1, 2) == 11
        assert StringBoard.index(1, 3) == 12
        assert StringBoard.index(1, 4) == 13
        assert StringBoard.index(1, 5) == 14
        assert StringBoard.index(1, 6) == 15
        assert StringBoard.index(1, 7) == 16
        assert StringBoard.index(1, 8) == 17

        assert StringBoard.index(2, 0) == 18
        assert StringBoard.index(2, 1) == 19
        assert StringBoard.index(2, 2) == 20
        assert StringBoard.index(2, 3) == 21
        assert StringBoard.index(2, 4) == 22
        assert StringBoard.index(2, 5) == 23
        assert StringBoard.index(2, 6) == 24
        assert StringBoard.index(2, 7) == 25
        assert StringBoard.index(2, 8) == 26

        assert StringBoard.index(3, 0) == 27
        assert StringBoard.index(3, 1) == 28
        assert StringBoard.index(3, 2) == 29
        assert StringBoard.index(3, 3) == 30
        assert StringBoard.index(3, 4) == 31
        assert StringBoard.index(3, 5) == 32
        assert StringBoard.index(3, 6) == 33
        assert StringBoard.index(3, 7) == 34
        assert StringBoard.index(3, 8) == 35

        assert StringBoard.index(4, 0) == 36
        assert StringBoard.index(4, 1) == 37
        assert StringBoard.index(4, 2) == 38
        assert StringBoard.index(4, 3) == 39
        assert StringBoard.index(4, 4) == 40
        assert StringBoard.index(4, 5) == 41
        assert StringBoard.index(4, 6) == 42
        assert StringBoard.index(4, 7) == 43
        assert StringBoard.index(4, 8) == 44

        assert StringBoard.index(5, 0) == 45
        assert StringBoard.index(5, 1) == 46
        assert StringBoard.index(5, 2) == 47
        assert StringBoard.index(5, 3) == 48
        assert StringBoard.index(5, 4) == 49
        assert StringBoard.index(5, 5) == 50
        assert StringBoard.index(5, 6) == 51
        assert StringBoard.index(5, 7) == 52
        assert StringBoard.index(5, 8) == 53

        assert StringBoard.index(6, 0) == 54
        assert StringBoard.index(6, 1) == 55
        assert StringBoard.index(6, 2) == 56
        assert StringBoard.index(6, 3) == 57
        assert StringBoard.index(6, 4) == 58
        assert StringBoard.index(6, 5) == 59
        assert StringBoard.index(6, 6) == 60
        assert StringBoard.index(6, 7) == 61
        assert StringBoard.index(6, 8) == 62

        assert StringBoard.index(7, 0) == 63
        assert StringBoard.index(7, 1) == 64
        assert StringBoard.index(7, 2) == 65
        assert StringBoard.index(7, 3) == 66
        assert StringBoard.index(7, 4) == 67
        assert StringBoard.index(7, 5) == 68
        assert StringBoard.index(7, 6) == 69
        assert StringBoard.index(7, 7) == 70
        assert StringBoard.index(7, 8) == 71

        assert StringBoard.index(8, 0) == 72
        assert StringBoard.index(8, 1) == 73
        assert StringBoard.index(8, 2) == 74
        assert StringBoard.index(8, 3) == 75
        assert StringBoard.index(8, 4) == 76
        assert StringBoard.index(8, 5) == 77
        assert StringBoard.index(8, 6) == 78
        assert StringBoard.index(8, 7) == 79
        assert StringBoard.index(8, 8) == 80

    def test_string_board_numbers(self):
        """
        1: ... 6.. ...
        2: 874 ... ...
        3: ... .3. .97
        4: .67 9.. .5.
        5: 9.. 1.6 ..8
        6: .8. ..3 16.
        7: 72. .8. ...
        8: ... ... 935
        9: ... ..1 ...
        """

        sut =StringBoard('...6.....874..........3..97.679...5.9..1.6..8.8...316.72..8..........935.....1...')

        assert sut.cell(1, 1) == Cell(0, Coordinates((1, 1)))
        assert sut.cell(1, 2) == Cell(0, Coordinates((1, 2)))
        assert sut.cell(1, 3) == Cell(0, Coordinates((1, 3)))
        assert sut.cell(1, 4) == Cell(6, Coordinates((1, 4)))
        assert sut.cell(1, 5) == Cell(0, Coordinates((1, 5)))
        assert sut.cell(1, 6) == Cell(0, Coordinates((1, 6)))
        assert sut.cell(1, 7) == Cell(0, Coordinates((1, 7)))
        assert sut.cell(1, 8) == Cell(0, Coordinates((1, 8)))
        assert sut.cell(1, 9) == Cell(0, Coordinates((1, 9)))

        assert sut.cell(2, 1) == Cell(8, Coordinates((2, 1)))
        assert sut.cell(2, 2) == Cell(7, Coordinates((2, 2)))
        assert sut.cell(2, 3) == Cell(4, Coordinates((2, 3)))
        assert sut.cell(2, 4) == Cell(0, Coordinates((2, 4)))
        assert sut.cell(2, 5) == Cell(0, Coordinates((2, 5)))
        assert sut.cell(2, 6) == Cell(0, Coordinates((2, 6)))
        assert sut.cell(2, 7) == Cell(0, Coordinates((2, 7)))
        assert sut.cell(2, 8) == Cell(0, Coordinates((2, 8)))
        assert sut.cell(2, 9) == Cell(0, Coordinates((2, 9)))

        assert sut.cell(3, 1) == Cell(0, Coordinates((3, 1)))
        assert sut.cell(3, 2) == Cell(0, Coordinates((3, 2)))
        assert sut.cell(3, 3) == Cell(0, Coordinates((3, 3)))
        assert sut.cell(3, 4) == Cell(0, Coordinates((3, 4)))
        assert sut.cell(3, 5) == Cell(3, Coordinates((3, 5)))
        assert sut.cell(3, 6) == Cell(0, Coordinates((3, 6)))
        assert sut.cell(3, 7) == Cell(0, Coordinates((3, 7)))
        assert sut.cell(3, 8) == Cell(9, Coordinates((3, 8)))
        assert sut.cell(3, 9) == Cell(7, Coordinates((3, 9)))

        assert sut.cell(4, 1) == Cell(0, Coordinates((4, 1)))
        assert sut.cell(4, 2) == Cell(6, Coordinates((4, 2)))
        assert sut.cell(4, 3) == Cell(7, Coordinates((4, 3)))
        assert sut.cell(4, 4) == Cell(9, Coordinates((4, 4)))
        assert sut.cell(4, 5) == Cell(0, Coordinates((4, 5)))
        assert sut.cell(4, 6) == Cell(0, Coordinates((4, 6)))
        assert sut.cell(4, 7) == Cell(0, Coordinates((4, 7)))
        assert sut.cell(4, 8) == Cell(5, Coordinates((4, 8)))
        assert sut.cell(4, 9) == Cell(0, Coordinates((4, 9)))

        assert sut.cell(5, 1) == Cell(9, Coordinates((5, 1)))
        assert sut.cell(5, 2) == Cell(0, Coordinates((5, 2)))
        assert sut.cell(5, 3) == Cell(0, Coordinates((5, 3)))
        assert sut.cell(5, 4) == Cell(1, Coordinates((5, 4)))
        assert sut.cell(5, 5) == Cell(0, Coordinates((5, 5)))
        assert sut.cell(5, 6) == Cell(6, Coordinates((5, 6)))
        assert sut.cell(5, 7) == Cell(0, Coordinates((5, 7)))
        assert sut.cell(5, 8) == Cell(0, Coordinates((5, 8)))
        assert sut.cell(5, 9) == Cell(8, Coordinates((5, 9)))

        assert sut.cell(6, 1) == Cell(0, Coordinates((6, 1)))
        assert sut.cell(6, 2) == Cell(8, Coordinates((6, 2)))
        assert sut.cell(6, 3) == Cell(0, Coordinates((6, 3)))
        assert sut.cell(6, 4) == Cell(0, Coordinates((6, 4)))
        assert sut.cell(6, 5) == Cell(0, Coordinates((6, 5)))
        assert sut.cell(6, 6) == Cell(3, Coordinates((6, 6)))
        assert sut.cell(6, 7) == Cell(1, Coordinates((6, 7)))
        assert sut.cell(6, 8) == Cell(6, Coordinates((6, 8)))
        assert sut.cell(6, 9) == Cell(0, Coordinates((6, 9)))

        assert sut.cell(7, 1) == Cell(7, Coordinates((7, 1)))
        assert sut.cell(7, 2) == Cell(2, Coordinates((7, 2)))
        assert sut.cell(7, 3) == Cell(0, Coordinates((7, 3)))
        assert sut.cell(7, 4) == Cell(0, Coordinates((7, 4)))
        assert sut.cell(7, 5) == Cell(8, Coordinates((7, 5)))
        assert sut.cell(7, 6) == Cell(0, Coordinates((7, 6)))
        assert sut.cell(7, 7) == Cell(0, Coordinates((7, 7)))
        assert sut.cell(7, 8) == Cell(0, Coordinates((7, 8)))
        assert sut.cell(7, 9) == Cell(0, Coordinates((7, 9)))

        assert sut.cell(8, 1) == Cell(0, Coordinates((8, 1)))
        assert sut.cell(8, 2) == Cell(0, Coordinates((8, 2)))
        assert sut.cell(8, 3) == Cell(0, Coordinates((8, 3)))
        assert sut.cell(8, 4) == Cell(0, Coordinates((8, 4)))
        assert sut.cell(8, 5) == Cell(0, Coordinates((8, 5)))
        assert sut.cell(8, 6) == Cell(0, Coordinates((8, 6)))
        assert sut.cell(8, 7) == Cell(9, Coordinates((8, 7)))
        assert sut.cell(8, 8) == Cell(3, Coordinates((8, 8)))
        assert sut.cell(8, 9) == Cell(5, Coordinates((8, 9)))

        assert sut.cell(9, 1) == Cell(0, Coordinates((9, 1)))
        assert sut.cell(9, 2) == Cell(0, Coordinates((9, 2)))
        assert sut.cell(9, 3) == Cell(0, Coordinates((9, 3)))
        assert sut.cell(9, 4) == Cell(0, Coordinates((9, 4)))
        assert sut.cell(9, 5) == Cell(0, Coordinates((9, 5)))
        assert sut.cell(9, 6) == Cell(1, Coordinates((9, 6)))
        assert sut.cell(9, 7) == Cell(0, Coordinates((9, 7)))
        assert sut.cell(9, 8) == Cell(0, Coordinates((9, 8)))
        assert sut.cell(9, 9) == Cell(0, Coordinates((9, 9)))