import random

# CLI based minesweeper
# play the game


class Board:
    def __init__(self, dim_size, num_bombs):
        # keep track of parameters
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # create the board
        self.board = self.make_new_board()  # plant the bombs
        self.assign_values_to_board()

        # initialize a set to keep track of locations covered
        self.dug = set()

    def make_new_board(self):
        # construct a new board based on the dim size and num bombs

        # generate a new board

        board = [[None for _ in range(self.dim_size)]
                 for _ in range(self.dim_size)]

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                # bombs planted, keep going
                continue

            board[row][col] = '*'  # plant bombs
            bombs_planted += 1

        return board


def play(dim_size=10, num_bombs=10):
    pass
