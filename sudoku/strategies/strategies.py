# https://www.sudopedia.org/wiki/Hidden_Single
from enum import Enum, auto

from sudoku.board.board_manager import BoardManager
from sudoku.strategies.hidden_single.block_hidden_single import BlockHiddenSingle
from sudoku.strategies.hidden_single.column_hidden_single import ColumnHiddenSingle
from sudoku.strategies.hidden_single.line_hidden_single import LineHiddenSingle
from sudoku.strategies.naked_simple.naked_single import NakedSingle
from sudoku.strategies.simple_elimination.simple_elimination import SimpleElimination


class Strategies(Enum):
    SIMPLE_ELIMINATION = auto()
    NAKED_SINGLE = auto()
    LINE_HIDDEN_SINGLE = auto()
    COLUMN_HIDDEN_SINGLE = auto()
    BLOCK_HIDDEN_SINGLE = auto()

    def get(self, board: BoardManager):
        if self is Strategies.SIMPLE_ELIMINATION:
            return SimpleElimination(board)
        if self is Strategies.NAKED_SINGLE:
            return NakedSingle(board)
        if self is Strategies.LINE_HIDDEN_SINGLE:
            return LineHiddenSingle(board)
        if self is Strategies.COLUMN_HIDDEN_SINGLE:
            return ColumnHiddenSingle(board)
        if self is Strategies.BLOCK_HIDDEN_SINGLE:
            return BlockHiddenSingle(board)
        return None

    def run(self, board: BoardManager) -> None:
        """"""
        strategy = self.get(board)
        if strategy.trigger:
            strategy.iterate()
