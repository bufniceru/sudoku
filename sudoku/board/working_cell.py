

from sudoku.board.board import Board
from sudoku.board.cell import Cell
from sudoku.config.constants import ALL_POSSIBILITIES_SET


class WorkingCell(Board, Cell):
    """
    This Class keeps reference of a current CELL involved in Solving Logic
    In addition to a Simple CELL it can gather information related to:
     - LINE that contains it
     - COLUMN that contains it
     - BLOCK that contains it
    It needs a reference to the BOARD that contains it in order to obtain information related to its neighbours.
    """
    def __init__(self, board: Board, cell: Cell):
        super().__init__()
        self.__dict__.update(board.__dict__)
        self.__dict__.update(cell.__dict__)

    def markup_discard_neighbours(self):
        """DEliminate Markup element according to the neigbours
        from Line, Column and Block.
        """
        for neighbour_number in self.neighbours_numbers:
            self.markup.discard(neighbour_number)

    def is_possible(self, number):
        """Check if a number is a Canditate to this Cell
        """
        return number in self.possible_numbers

    @property
    def neighbours_numbers(self):
        """Return The Set of Numbers found on the Line, Column and Block
        that own the Empty Cell is Created by Union
        """
        return self.line_numbers.union(
            self.column_numbers).union(
            self.block_numbers)

    @property
    def possible_numbers(self):
        """Return The set of possible number to be Cndidates in the Cell according to
        the neigbouts in Line, Column and Block.
        In fact, it is the markup of the Cell
        """
        return self.line_possible_numbers.intersection(
            self.column_possible_numbers).intersection(
            self.block_possible_numbers)

    @property
    def line(self):
        """Return a list with the Cells of the LINE to whom the Cell belongs
        """
        clip = self.grid[self.coordinates.line - 1, :]
        return list([cell() for cell in clip])

    @property
    def line_numbers(self):
        """Return a set with the cell numbers of the LINE to whom the Cell belongs
        """
        return set([value for value in self.line if value != 0])

    @property
    def line_possible_numbers(self):
        """Return a set with the possible numbers of the Cell from LINE point of view
        """
        return ALL_POSSIBILITIES_SET - self.line_numbers

    #
    # COLUMNS
    #
    @property
    def column(self):
        """Return a list with the Cells of the COLUMN to whom the Cell belongs
        """
        clip =  self.grid[:, self.coordinates.column - 1]
        return list([cell() for cell in clip])

    @property
    def column_numbers(self):
        """Return a set with the cell numbers of the COLUMN to whom the Cell belongs
        """
        return set([value for value in self.column if value != 0])

    @property
    def column_possible_numbers(self):
        """Return a set with the possible numbers of the Cell from COLUMN point of view
        """
        return ALL_POSSIBILITIES_SET - self.column_numbers

    #
    # BLOCKS
    #
    @property
    def block(self):
        """Return a list with the Cells of the BLOCK to whom the Cell belongs
        """
        clip =  self.grid[self.coordinates.block_line_start:self.coordinates.block_line_finish,
                                 self.coordinates.block_column_start:self.coordinates.block_column_finish]
        return list([cell() for cell in clip.flatten()])

    @property
    def block_numbers(self):
        """Return a set with the cell numbers of the BLOCK to whom the Cell belongs
        """
        return set([value for value in self.block if value != 0])

    @property
    def block_possible_numbers(self):
        """Return a set with the possible numbers of the Cell from BLOCK point of view
        """
        return ALL_POSSIBILITIES_SET - self.block_numbers

    def __call__(self):
        return Cell.__call__(self)

    def __str__(self):
        return Cell.__str__(self)