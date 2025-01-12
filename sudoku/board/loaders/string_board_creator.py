from sudoku.board.board import Board
from sudoku.board.helpers.coordinates import Coordinates
from sudoku.config.constants import ALL_POSSIBILITIES_SET


class StringBoardCreator:
    @staticmethod
    def create_board(problem_string) -> Board:
        problem_string = problem_string.replace('.', '0')
        board = Board()
        for board_line, line in enumerate([problem_string[i:i + 9] for i in range(0, len(problem_string), 9)]):
            for board_column, char in enumerate(line):
                if int(char) in ALL_POSSIBILITIES_SET:
                    board(Coordinates((board_line + 1, board_column + 1))).value = int(char)
        return board
