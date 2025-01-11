from sudoku.board.board_manager import BoardManager
from sudoku.board.helpers.coordinates import Coordinates
from sudoku.board.loaders.string_board import StringBoard
from sudoku.board.loaders.string_board_creator import StringBoardCreator
from sudoku.board.working_cell import WorkingCell
from sudoku.config.constants import BOARD_DIMENSION, ALL_POSSIBILITIES_SET, EMPTY_SET


sudoku_grid = "...6.....874..........3..97.679...5.9..1.6..8.8...316.72..8..........935.....1..."

class TestBoardManager:
    def test_board_manager_constructor(self):

        sut = BoardManager()

        assert sut.validity is True
        assert sut.blanks == 81
        assert sut.givens == 0

        assert sut.grid.shape == (9,9)
        assert sut.grid.ndim == 2

        for line in range(0, BOARD_DIMENSION):
            for column in range(0, BOARD_DIMENSION):
                assert sut.grid[line][column]() == 0
                assert sut.grid[line][column].markup.value == ALL_POSSIBILITIES_SET
                assert sut.grid[line][column].coordinates.line == line + 1
                assert sut.grid[line][column].coordinates.column == column + 1

    def test_board_string_board_creator(self):

        string_board = StringBoard(sudoku_grid)

        sut = BoardManager(StringBoardCreator.create_board(string_board.string))

        assert sut.validity is True
        assert sut.blanks == 55
        assert sut.givens == 26
        assert sut.how_many(1) == 3
        assert sut.how_many(2) == 1
        assert sut.how_many(3) == 3
        assert sut.how_many(4) == 1
        assert sut.how_many(5) == 2
        assert sut.how_many(6) == 4
        assert sut.how_many(7) == 4
        assert sut.how_many(8) == 4
        assert sut.how_many(9) == 4

        assert sut.grid.shape == (9,9)
        assert sut.grid.ndim == 2

        for line in range(0, BOARD_DIMENSION):
            for column in range(0, BOARD_DIMENSION):
                if sut.grid[line][column]() == 0:
                    assert sut.grid[line][column].markup.value == ALL_POSSIBILITIES_SET
                else:
                    assert sut.grid[line][column].markup.value == EMPTY_SET
                assert sut.grid[line][column].coordinates.line == line + 1
                assert sut.grid[line][column].coordinates.column == column + 1
                assert sut.grid[line][column] == string_board.cell(line + 1, column + 1)

        assert sut.current_cell.value.value is None
        assert sut.current_cell.markup.value == ALL_POSSIBILITIES_SET
        assert sut.current_cell.coordinates.line == 1
        assert sut.current_cell.coordinates.column == 1

        sut.current_cell = WorkingCell(sut, sut(Coordinates((5,9))))

        assert sut.current_cell.value.value == 8
        assert sut.current_cell.markup.value == EMPTY_SET
        assert sut.current_cell.coordinates.line == 5
        assert sut.current_cell.coordinates.column == 9

        sut.current_cell = WorkingCell(sut, sut(Coordinates((9,9))))

        assert sut.current_cell.value.value is None
        assert sut.current_cell.markup.value == ALL_POSSIBILITIES_SET
        assert sut.current_cell.coordinates.line == 9
        assert sut.current_cell.coordinates.column == 9

    def test_board_lines(self):

        string_board = StringBoard(sudoku_grid)

        sut = BoardManager(StringBoardCreator.create_board(string_board.string))

        assert sut.current_cell.line == [0, 0, 0, 6, 0, 0, 0, 0, 0]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((2,1))))
        assert sut.current_cell.line == [8, 7, 4, 0, 0, 0, 0, 0, 0]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((3,1))))
        assert sut.current_cell.line == [0, 0, 0, 0, 3, 0, 0, 9, 7]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((4,1))))
        assert sut.current_cell.line == [0, 6, 7, 9, 0, 0, 0, 5, 0]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((5,1))))
        assert sut.current_cell.line == [9, 0, 0, 1, 0, 6, 0, 0, 8]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((6,1))))
        assert sut.current_cell.line == [0, 8, 0, 0, 0, 3, 1, 6, 0]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((7,1))))
        assert sut.current_cell.line == [7, 2, 0, 0, 8, 0, 0, 0, 0]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((8,1))))
        assert sut.current_cell.line == [0, 0, 0, 0, 0, 0, 9, 3, 5]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((9,1))))
        assert sut.current_cell.line == [0, 0, 0, 0, 0, 1, 0, 0, 0]

    def test_board_line_numbers(self):

        string_board = StringBoard(sudoku_grid)

        sut = BoardManager(StringBoardCreator.create_board(string_board.string))

        assert sut.current_cell.line_numbers == {6}
        sut.current_cell = WorkingCell(sut, sut(Coordinates((2,1))))
        assert sut.current_cell.line_numbers == {4, 7, 8}
        sut.current_cell = WorkingCell(sut, sut(Coordinates((3,1))))
        assert sut.current_cell.line_numbers == {3, 7, 9}
        sut.current_cell = WorkingCell(sut, sut(Coordinates((4,1))))
        assert sut.current_cell.line_numbers == {5, 6, 7, 9}
        sut.current_cell = WorkingCell(sut, sut(Coordinates((5,1))))
        assert sut.current_cell.line_numbers == {1, 6, 8, 9}
        sut.current_cell = WorkingCell(sut, sut(Coordinates((6,1))))
        assert sut.current_cell.line_numbers == {1, 3, 6, 8}
        sut.current_cell = WorkingCell(sut, sut(Coordinates((7,1))))
        assert sut.current_cell.line_numbers == {2, 7, 8}
        sut.current_cell = WorkingCell(sut, sut(Coordinates((8,1))))
        assert sut.current_cell.line_numbers == {3, 5, 9}
        sut.current_cell = WorkingCell(sut, sut(Coordinates((9,1))))
        assert sut.current_cell.line_numbers == {1}

    def test_board_columns(self):

        string_board = StringBoard(sudoku_grid)

        sut = BoardManager(StringBoardCreator.create_board(string_board.string))

        assert sut.current_cell.column == [0, 8, 0, 0, 9, 0, 7, 0, 0]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((1,2))))
        assert sut.current_cell.column == [0, 7, 0, 6, 0, 8, 2, 0, 0]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((1,3))))
        assert sut.current_cell.column == [0, 4, 0, 7, 0, 0, 0, 0, 0]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((1,4))))
        assert sut.current_cell.column == [6, 0, 0, 9, 1, 0, 0, 0, 0]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((1,5))))
        assert sut.current_cell.column == [0, 0, 3, 0, 0, 0, 8, 0, 0]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((1,6))))
        assert sut.current_cell.column == [0, 0, 0, 0, 6, 3, 0, 0, 1]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((1,7))))
        assert sut.current_cell.column == [0, 0, 0, 0, 0, 1, 0, 9, 0]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((1,8))))
        assert sut.current_cell.column == [0, 0, 9, 5, 0, 6, 0, 3, 0]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((1,9))))
        assert sut.current_cell.column == [0, 0, 7, 0, 8, 0, 0, 5, 0]

    def test_board_blocks(self):

        string_board = StringBoard(sudoku_grid)

        sut = BoardManager(StringBoardCreator.create_board(string_board.string))

        assert sut.current_cell.block == [0, 0, 0, 8, 7, 4, 0, 0, 0]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((1,4))))
        assert sut.current_cell.block == [6, 0, 0, 0, 0, 0, 0, 3, 0]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((1,7))))
        assert sut.current_cell.block == [0, 0, 0, 0, 0, 0, 0, 9, 7]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((4,1))))
        assert sut.current_cell.block == [0, 6, 7, 9, 0, 0, 0, 8, 0]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((4,4))))
        assert sut.current_cell.block == [9, 0, 0, 1, 0, 6, 0, 0, 3]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((4,7))))
        assert sut.current_cell.block == [0, 5, 0, 0, 0, 8, 1, 6, 0]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((7,1))))
        assert sut.current_cell.block == [7, 2, 0, 0, 0, 0, 0, 0, 0]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((7,4))))
        assert sut.current_cell.block == [0, 8, 0, 0, 0, 0, 0, 0, 1]
        sut.current_cell = WorkingCell(sut, sut(Coordinates((7,7))))
        assert sut.current_cell.block == [0, 0, 0, 9, 3, 5, 0, 0, 0]

    def test_board_neighbours(self):

        string_board = StringBoard(sudoku_grid)

        sut = BoardManager(StringBoardCreator.create_board(string_board.string))

        assert sut.current_cell.neighbours_numbers == {4, 6, 7, 8, 9}

    def test_board_possible(self):

        string_board = StringBoard(sudoku_grid)

        sut = BoardManager(StringBoardCreator.create_board(string_board.string))

        assert sut.current_cell.possible_numbers == {1, 2, 3, 5}

        assert (1 in sut.current_cell.possible_numbers) is True
        assert (2 in sut.current_cell.possible_numbers) is True
        assert (3 in sut.current_cell.possible_numbers) is True
        assert (5 in sut.current_cell.possible_numbers) is True

    def test_board_scan_empty_cells(self):

        string_board = StringBoard(sudoku_grid)

        sut = BoardManager(StringBoardCreator.create_board(string_board.string))

        print('\n')
        for cell in sut.scan_empty_cells():
            print(cell(), end="")
        print()

    def test_board_scan_non_empty_cells(self):

        string_board = StringBoard(sudoku_grid)

        sut = BoardManager(StringBoardCreator.create_board(string_board.string))

        print('\n')
        for cell in sut.scan_non_empty_cells():
            print(cell(), end="")
        print()

    def test_board_scan_cells(self):

        string_board = StringBoard(sudoku_grid)

        sut = BoardManager(StringBoardCreator.create_board(string_board.string))

        line = 1
        column = 1
        for cell in sut.scan_cells():
            assert cell.coordinates.line == line
            assert cell.coordinates.column == column
            if column < 9:
                column += 1
            else:
                column = 1
                line += 1

    def test_board_find_first_empty_cell(self):

        string_board = StringBoard(sudoku_grid)

        sut = BoardManager(StringBoardCreator.create_board(string_board.string))

        assert sut.find_first_empty_cell()() == 0
        assert sut.find_first_empty_cell().coordinates.line == 1
        assert sut.find_first_empty_cell().coordinates.column == 1
