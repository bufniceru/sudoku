from sudoku.board.board_manager import BoardManager
from sudoku.board.loaders.string_board import StringBoard
from sudoku.board.loaders.string_board_creator import StringBoardCreator
from sudoku.board.output.board_log_output import BoardLogOutput
from sudoku.strategies.strategies import Strategies

sudoku_grid = "..1.....2.2.....1.3...2.......3.1....5.....9....7.4.......8...3.1.....5.6.....4.."

class TestLineHiddenSingle:
    def test_line_hidden_single(self):

        string_board = StringBoard(sudoku_grid)

        board = StringBoardCreator.create_board(string_board.string)

        prnt = BoardLogOutput(board)

        prnt.full()

        board_manager = BoardManager(board)

        Strategies.SIMPLE_ELIMINATION.run(board_manager)

        prnt.full()

        Strategies.NAKED_SINGLE.run(board_manager)

        prnt.full()

        Strategies.SIMPLE_ELIMINATION.run(board_manager)

        prnt.full()

        Strategies.LINE_HIDDEN_SINGLE.run(board_manager)

        prnt.full()

        Strategies.SIMPLE_ELIMINATION.run(board_manager)

        prnt.full()

        Strategies.LINE_HIDDEN_SINGLE.run(board_manager)

        prnt.full()

        Strategies.SIMPLE_ELIMINATION.run(board_manager)

        prnt.full()

        Strategies.LINE_HIDDEN_SINGLE.run(board_manager)

        prnt.full()
