from icecream import ic


class LineHiddenSingle:

    name = "LINE HIDDEN SINGLE"

    def __init__(self, board):
        self.board = board
        self.found_cell = None
        self.found_value = None

    @property
    def trigger(self):
        self.found_cell, self.found_value = self.board.find_first_line_hidden_single()
        return self.found_cell

    def iterate(self):
        if self.found_cell:
            ic(f"{LineHiddenSingle.name} {self.found_cell} = {self.found_value}")
            self.found_cell.promote_hidden_single(self.found_value)
