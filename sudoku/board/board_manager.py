from typing import Generator

from icecream import ic

from sudoku.board.cell import Cell
from sudoku.board.working_cell import WorkingCell
from sudoku.board.board import Board
from sudoku.board.helpers.coordinates import Coordinates
from sudoku.config.constants import BOARD_DIMENSION


class BoardManager(Board):
    """Involves some solving logic in addition to a Simple BOARD.
    It needs a Current CELL that scan the BOARD for different purposes.
    """
    def __init__(self, board: Board = None) -> None:
        super().__init__()
        if board is not None:
            self.__dict__.update(board.__dict__)
        self.current_cell = WorkingCell(self, self(Coordinates((1,1))))

    def find_first_empty_cell(self) -> Cell | None:
        """Return First Empty Cell if found
        If there is no Cell found then the Sudoku is Solved.
        """
        for cell in self.scan_empty_cells():
            return cell
        else:
            return None

    def find_first_naked_single(self) -> (Cell, int):
        """Return First Naked Single Cell if found."""
        for cell in self.scan_empty_cells():
            cell_naked_set = cell.markup.value
            # ic(f"NAKED CELL {cell} = {next(iter(cell_naked_set))}")
            if len(cell_naked_set) == 1:
                return cell, next(iter(cell_naked_set))
        else:
            return None, None

    def find_first_line_hidden_single(self) -> (Cell, int):
        """Return First Line Hidden Single Cell if found."""
        for cell in self.scan_empty_cells():
            cell_hidden_set = cell.possible_numbers - cell.line_possible_numbers_except_me
            if len(cell_hidden_set) == 1:
                # ic(f"LINE HIDDEN CELL {cell} = {next(iter(cell_hidden_set))}")
                return cell, next(iter(cell_hidden_set))
        else:
            return None, None

    def find_first_column_hidden_single(self) -> (Cell, int):
        """Return First Column Hidden Single Cell if found."""
        for cell in self.scan_empty_cells():
            cell_hidden_set = cell.possible_numbers - cell.column_possible_numbers_except_me
            if len(cell_hidden_set) == 1:
                # ic(f"COLUMN HIDDEN CELL {cell} = {next(iter(cell_hidden_set))}")
                return cell, next(iter(cell_hidden_set))
        else:
            return None, None

    def find_first_block_hidden_single(self) -> (Cell, int):
        """Return First Block Hidden Single Cell if found."""
        for cell in self.scan_empty_cells():
            cell_hidden_set = cell.possible_numbers - cell.block_possible_numbers_except_me
            if len(cell_hidden_set) == 1:
                # ic(f"BLOCK HIDDEN CELL {cell} = {next(iter(cell_hidden_set))}")
                return cell, next(iter(cell_hidden_set))
        else:
            return None, None

    def scan_empty_cells(self) -> Generator[WorkingCell, None, None]:
        """Scan the Board for empty cells."""
        for cell in self.scan_cells():
            if cell.value.value is None:
                self.current_cell = WorkingCell(self, self(Coordinates((cell.coordinates.line, cell.coordinates.column))))
                yield self.current_cell

    def scan_non_empty_cells(self) -> Generator[WorkingCell, None, None]:
        """Scan the Board for non empty cells."""
        for cell in self.scan_cells():
            if cell.value.value is not None:
                yield cell

    def scan_cells(self) -> Generator[WorkingCell, None, None]:
        """Scan the Board for all cells. Line by Line, Column by Column."""
        for line_no in range(1, BOARD_DIMENSION + 1):
            for column_no in range(1, BOARD_DIMENSION + 1):
                yield self(Coordinates((line_no, column_no)))
