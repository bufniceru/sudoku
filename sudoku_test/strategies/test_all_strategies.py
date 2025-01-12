from sudoku.board.board_manager import BoardManager
from sudoku.board.loaders.string_board import StringBoard
from sudoku.board.loaders.string_board_creator import StringBoardCreator
from sudoku.board.output.board_log_output import BoardLogOutput
from sudoku.strategies.strategies import Strategies

# sudoku_grid = "..1.....2.2.....1.3...2.......3.1....5.....9....7.4.......8...3.1.....5.6.....4.."
sudoku_grid = "1..2..3...2..1..4...3..5..67..6..5...5..8..7...8..4..18..7..4...3..6..2...9..2..7"

class TestNakedSingle:
    def test_naked_single(self):

        string_board = StringBoard(sudoku_grid)

        board = StringBoardCreator.create_board(string_board.string)

        prnt = BoardLogOutput(board)

        board_manager = BoardManager(board)

        Strategies.SIMPLE_ELIMINATION.run(board_manager)

        prnt.full()

        given_initial = board_manager.givens

        for _ in range(100):
            Strategies.NAKED_SINGLE.run(board_manager)
            Strategies.SIMPLE_ELIMINATION.run(board_manager)
            Strategies.LINE_HIDDEN_SINGLE.run(board_manager)
            Strategies.SIMPLE_ELIMINATION.run(board_manager)
            Strategies.COLUMN_HIDDEN_SINGLE.run(board_manager)
            Strategies.SIMPLE_ELIMINATION.run(board_manager)
            Strategies.BLOCK_HIDDEN_SINGLE.run(board_manager)
            Strategies.SIMPLE_ELIMINATION.run(board_manager)

            given_iteration = board_manager.givens

            if given_initial == given_iteration:
                break

        prnt.full()
