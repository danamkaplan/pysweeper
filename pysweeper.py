import random

class Cell(object):
    
    def __init__(self):
        self.flag = False
        self.bomb = False
        self.bomb_neighbors = 0
        self.revealed = False

    def set_bomb(self):
        self.bomb = True

    def bomb_check(self):
        return self.bomb

    def set_neighbors(self, amount):
        self.bomb_neighbors = amount

    def get_neighbors(self):
        return self.bomb_neighbors

    def set_flag(self):
        self.flag = True

    def get_flag(self):
        return self.flag

    def reveal(self):
        self.revealed = True
    
    def is_revealed(self)
        return revealed

class Grid(object):

    def __init__(self, row_size=8, col_size=8, bomb_amount=9):
        self.row_size = row_size
        self.col_size = col_size
        self.bombs_remaining = bomb_amount
        self.bombs_not_planted = bomb_amount
        self.create_board()

    def populate_grid(self):
        self.grid_matrix = []
        for row_position in xrange(row_size):
            self.grid_matrix[row_position] = []
            for col_position in xrange(col_size):
                self.grid_matrix[row_position].append(Cell())

    def plant_bombs(self):
        # randomnly place some bombs
        while self.bombs_not_planted > 0:
            rand_row = random.randint(0, self.row_size-1)
            rand_col = random.randint(0, self.col_size-1)
            if not self.grid_matrix[rand_row][rand_col].bomb_check():
                self.grid_matrix[rand_row][rand_col].set_bomb()
                self.bombs_not_planted -= 1

    def calculate_neighbor(self, row, col):
        neighbor_counter = 0 
        for n_row in xrange(row-1, 2):
            for n_col in xrange(col-1, 2):
                try: 
                    if self.grid_matrix[n_row][n_col].bomb_check():
                        neighbor_counter += 1
                except IndexError:
                    continue

        if not self.grid_matrix[row][col].bomb_check():
            self.grid_matrix[row][col].set_neighbors(neighbor_counter)

    def create_board(self):
        self.populate_grid()
        self.plant_bombs()
        [calculate_neighbor(r,c) for r in xrange(self.row_size) for c in
                xrange(self.col_size)]
