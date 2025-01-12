from sudoku.board.board_manager import BoardManager
from sudoku.board.loaders.string_board import StringBoard
from sudoku.board.loaders.string_board_creator import StringBoardCreator
from sudoku.board.output.board_log_output import BoardLogOutput
from sudoku.strategies.strategies import Strategies

sudoku_grid = "...6.....874..........3..97.679...5.9..1.6..8.8...316.72..8..........935.....1..."

class TestSimpleElimination:
    def test_simple_elimination(self):

        string_board = StringBoard(sudoku_grid)

        board = StringBoardCreator.create_board(string_board.string)

        prnt = BoardLogOutput(board)

        prnt.full()

        board_manager = BoardManager(board)

        Strategies.SIMPLE_ELIMINATION.run(board_manager)

        prnt.full()
