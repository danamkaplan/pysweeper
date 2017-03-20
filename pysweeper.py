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
        self.flag = not self.flag

    def is_flag(self):
        return self.flag

    def reveal(self):
        self.revealed = True
    
    def is_revealed(self):
        return self.revealed


class Grid(object):

    def __init__(self, row_size=8, col_size=8, bombs=9):
        self.row_size = row_size
        self.col_size = col_size
        self.bombs_remaining = bombs
        self.bombs_not_planted = bombs
        self.neighbor_dict = {}

    def populate_grid(self):
        self.grid_matrix = []
        for row_position in xrange(self.row_size):
            self.grid_matrix.append([])
            for col_position in xrange(self.col_size):
                self.grid_matrix[row_position].append(Cell())

    def plant_bombs(self, r, c):
        # randomnly place some bombs
        while self.bombs_not_planted > 0:
            rand_row = random.randint(0, self.row_size-1)
            rand_col = random.randint(0, self.col_size-1)
            if not self.grid_matrix[rand_row][rand_col].bomb_check():
                if rand_row != r and rand_col != c:
                    self.grid_matrix[rand_row][rand_col].set_bomb()
                    self.bombs_not_planted -= 1

        self.all_neighbors()
    
    def get_cell(self, row, col):
        return self.grid_matrix[row][col]

    def all_neighbors(self):
        for row in xrange(self.row_size):
            for col in xrange(self.col_size):
                self.calculate_neighbors(row, col)
                    
    def create_neighbors(self, row, col):
        self.neighbor_dict[(row, col)] = []
        # make a tuple dictionary of all neighbors
        # {
        # (r,c): [(r1,c2), (r2, c1)]
        # }
        
        for n_row in xrange(row-1, row+2):
            for n_col in xrange(col-1, col+2):
                if n_row in range(self.row_size) and\
                    n_col in range(self.col_size) and not\
                        (n_row == row and n_col == col):
                    self.neighbor_dict[(row, col)].append((n_row, n_col))

    def calculate_neighbors(self, row, col):
        neighbor_counter = 0 
        for n_cell in self.neighbor_dict[(row, col)]:
            if self.grid_matrix[n_cell[0]][n_cell[1]].bomb_check():
                neighbor_counter += 1
        self.grid_matrix[row][col].set_neighbors(neighbor_counter)

    def create_board(self):
        self.populate_grid()
        for r in xrange(self.row_size):
            for c in xrange(self.col_size):
                self.create_neighbors(r, c) 

    def return_bombs(self):
        bomb_matrix = [[False for r in xrange(self.row_size)] for c in xrange(self.col_size)]
        n_matrix = [[False for r in xrange(self.row_size)] for c in xrange(self.col_size)]
        for i in xrange(self.row_size):
            for j in xrange(self.col_size):
                bomb_matrix[i][j] = self.grid_matrix[i][j].bomb_check()
                n_matrix[i][j] = self.grid_matrix[i][j].get_neighbors()

        return (bomb_matrix, n_matrix)

    def reveal_cell(self, row, col, clicked):
        d = self.neighbor_dict[(row, col)]
        if self.grid_matrix[row][col].bomb_check() and clicked:
            return "end"
        self.grid_matrix[row][col].reveal()
        if self.grid_matrix[row][col].get_neighbors() == 0:
            for r, c in self.neighbor_dict[(row, col)]:
                if not self.grid_matrix[r][c].is_revealed():
                    self.reveal_cell(r, c, False)
    
    def draw_grid(self):
        # displays each cells status
        drawn_grid = []
        for row in xrange(self.row_size):
            drawn_grid.append([])
            for col in xrange(self.col_size):
                cell = self.grid_matrix
                if cell[row][col].is_revealed():
                    drawn_grid[row].append(str(cell[row][col].get_neighbors()))
                elif cell[row][col].is_flag():
                    drawn_grid[row].append("F")        
                else:
                    drawn_grid[row].append("#")

        return self.bombs_remaining, drawn_grid

    def get_neighbor_dict(self):
        return self.neighbor_dict

    def flag_cell(self, row, col):
        self.grid_matrix[row][col].set_flag()
        if self.grid_matrix[row][col].is_flag():
            self.bombs_remaining -= 1
        else:
            self.bombs_remaining += 1
    
    def win_state(self, bombs):
        r_count = 0
        for row in self.grid_matrix:
            for cell in row:
                if not cell.is_revealed():
                    r_count += 1
        if r_count <= bombs:
            return True
        else:
            return False


class Game(object):
    def __init__(self):
        pass
    
    def create_game(self, row=8, col=8, bombs=9):
        self.row = row
        self.col = col
        self.bombs = bombs
        self.finished = False
        
        # Create Grid object
        self.grid = Grid(row, col, bombs)

        # Populate the grid 
        self.grid.create_board()

    def draw_screen(self):
        self.bombs, screen = self.grid.draw_grid()
        if self.bombs == 0:
            self.finished = True
        x_axis = "  "+" ".join([str(i) for i in range(self.row)])
        print "---------"
        print "Bombs Remaining: {}".format(self.bombs)
        print x_axis
        print " "+"+-"*self.row+"+"
        for ix, row in enumerate(screen):
            s = "|".join([str(i) if i != '0' else " " for i in row])
            print "{}|{}|{}".format(ix, s, ix)
            print " "+"+-"*self.row+"+"
        print x_axis

    def control(self):
        action = raw_input("(C)lick or (F)lag cell?: ").lower()
        if action not in ["f", "c"]:
            "Not a choice."
            return self.control()
        row = int(raw_input("Which cell row?(Starting at 0): "))
        col = int(raw_input("Which cell column?(Starting at 0): "))
        if action == "f":
            self.grid.flag_cell(row, col)
        elif action == "c":
            state = self.grid.reveal_cell(row, col, True)
            if state == "end":
                self.finished = True

    def play_game(self):
        print "Welcome to the first game of the rest of your life"
        # first time setup
        self.draw_screen()
        print "Start by clicking which cell?" 
        row = int(raw_input("Which cell row?(Starting at 0): "))
        col = int(raw_input("Which cell column?(Starting at 0): "))
        self.grid.plant_bombs(row, col)
        self.grid.reveal_cell(row, col, True)

        # main game loop
        while not self.finished:
            self.draw_screen()
            self.control()

        if self.grid.win_state():
            print "YOU WIN!!!"
        else:
            print "YOU GOT BOMBED!!!"


if __name__ == '__main__':
    pass
