from sudoku.board.working_cell import WorkingCell
from sudoku.board.board import Board
from sudoku.board.helpers.coordinates import Coordinates
from sudoku.config.constants import BOARD_DIMENSION


class BoardManager(Board):
    """Involves some solving logic in addition to a Simple BOARD.
    It needs a Current CELL that scan the BOARD for different purposes.
    """
    def __init__(self, board: Board = None):
        super().__init__()
        if board is not None:
            self.__dict__.update(board.__dict__)
        self.current_cell = WorkingCell(self, self(Coordinates((1,1))))

    def find_first_empty_cell(self):
        """Return First Empty Cell if found
        If there is no Cell found then the Sudoku is Solved.
        """
        for cell in self.scan_empty_cells():
            return cell
        else:
            return None

    def find_first_naked_single(self):
        """Return First Naked Single Cell if found."""
        for cell in self.scan_empty_cells():
            if len(cell.markup.value) == 1:
                return cell
        else:
            return None

    def scan_empty_cells(self):
        """Scan the Board for empty cells."""
        for cell in self.scan_cells():
            if cell.value.value is None:
                self.current_cell = WorkingCell(self, self(Coordinates((cell.coordinates.line, cell.coordinates.column))))
                yield self.current_cell

    def scan_non_empty_cells(self):
        """Scan the Board for non empty cells."""
        for cell in self.scan_cells():
            if cell.value.value is not None:
                yield cell

    def scan_cells(self):
        """Scan the Board for all cells. Line by Line, Column by Column."""
        for line_no in range(1, BOARD_DIMENSION + 1):
            for column_no in range(1, BOARD_DIMENSION + 1):
                yield self(Coordinates((line_no, column_no)))
