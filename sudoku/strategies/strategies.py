from enum import Enum, auto

from sudoku.board.board_manager import BoardManager
from sudoku.strategies.naked_simple.naked_single import NakedSingle
from sudoku.strategies.simple_elimination.simple_elimination import SimpleElimination


class Strategies(Enum):
    SIMPLE_ELIMINATION = auto()
    NAKED_SINGLE = auto()

    def get(self, board: BoardManager):
        if self is Strategies.SIMPLE_ELIMINATION:
            return SimpleElimination(board)
        if self is Strategies.NAKED_SINGLE:
            return NakedSingle(board)

    def run(self, board: BoardManager):
        """"""
        strategy = self.get(board)
        if strategy.trigger:
            strategy.iterate()
