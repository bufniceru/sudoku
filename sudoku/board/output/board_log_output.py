from sudoku.board.helpers.coordinates import Coordinates
from sudoku.config.constants import ALL_POSSIBILITIES_SET, BOARD_DIMENSION


class BoardLogOutput:
    def __init__(self, board):
        self.board = board

    def bare(self):
        to_log = ""
        print("  123 456 789")
        print(" +---+---+---+")
        for line_no in range(1, BOARD_DIMENSION + 1):
            if line_no in {4, 7}:
                print(" +---+---+---+")
            to_log = f"{line_no}|"
            for column_no in range(1, BOARD_DIMENSION + 1):
                if column_no in {4, 7}:
                    to_log += "|"
                if self.board(Coordinates((line_no, column_no)))() != 0:
                    to_log += f"{self.board(Coordinates((line_no, column_no)))()}"
                if self.board(Coordinates((line_no, column_no)))() == 0:
                    to_log += " "
            to_log += "|"
            print(to_log)
        print(" +---+---+---+")
        print(f" Total Numbers {self.board.givens}")
        print("")

    def full(self):
        big_board = []
        for i in range(0, 27):
            big_board.append(list())
            for j in range(0, 27):
                big_board[i].append(" ")
        absolute_line = 0
        absolute_column = 0
        for start_block_line in range(0, 27, 3):
            for start_block_column in range(0, 27, 3):
                if len(self.board(Coordinates((absolute_line + 1, absolute_column + 1))).markup.value) != 0:
                    for elm in self.board(Coordinates((absolute_line + 1, absolute_column + 1))).markup.value:
                        big_board[start_block_line + ((elm - 1) // 3)][start_block_column + ((elm - 1) % 3)] = elm
                else:
                    for elm in ALL_POSSIBILITIES_SET:
                        big_board[start_block_line + ((elm - 1) // 3)][start_block_column + ((elm - 1) % 3)] = self.board(Coordinates((absolute_line + 1, absolute_column + 1)))()
                absolute_column += 1
            absolute_column = 0
            absolute_line += 1

        print("  111 222 333 444 555 666 777 888 999")
        print(" +---+---+---+---+---+---+---+---+---+")
        for big_line in range(0, 27):
            to_log = ""
            if big_line in {3, 6, 12, 15, 21, 24}:
                print(" +---+---+---+---+---+---+---+---+---+")
            if big_line in {9, 18}:
                print(" +---+---+---+---+---+---+---+---+---+")
            for big_column in range(0, 27):
                if big_column in {0}:
                    to_log += f"{big_line // 3 + 1}|"
                if big_column in {9, 18}:
                    to_log += "|"
                if big_column in {3, 6, 12, 15, 21, 24}:
                    to_log += "|"
                to_log += f"{big_board[big_line][big_column]}"
            to_log += f"|{big_line // 3 + 1}"
            print(to_log)
        print(" +---+---+---+---+---+---+---+---+---+")
        print("  111 222 333 444 555 666 777 888 999")
        print(f"EXISTING    [{self.board.givens}]")
        print(f"BOARD CHECK [{self.board.validity}]")
        print("")
