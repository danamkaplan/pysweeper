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

    def is_flag(self):
        return self.flag

    def reveal(self):
        self.revealed = True
    
    def is_revealed(self):
        return revealed


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

    def plant_bombs(self):
        # randomnly place some bombs
        while self.bombs_not_planted > 0:
            rand_row = random.randint(0, self.row_size-1)
            rand_col = random.randint(0, self.col_size-1)
            if not self.grid_matrix[rand_row][rand_col].bomb_check():
                self.grid_matrix[rand_row][rand_col].set_bomb()
                self.bombs_not_planted -= 1
    
    def get_cell(self, row, col):
        return self.grid_matrix[row][col]


    def create_neighbors(self, row, col):
        self.neighbor_dict[(row, col)] = []
        # make a tuple dictionary of all neighbors
        # {
        # (r,c): [(r1,c2), (r1, c2)]
        # }
        
        for n_row in xrange(row-1, row+2):
            for n_col in xrange(col-1, col+2):
                if n_row in range(self.row_size) and\
                    n_col in range(self.col_size) and not\
                    (n_row == row and n_col == col):
                    self.neighbor_dict[(row, col)].append((n_row, n_col))

    def calculate_neighbors(self, row, col):
        neighbor_counter = 0 
        for n_cell in self.neighbor_dict[(row,col)]:
            if self.grid_matrix[n_cell[0]][n_cell[1]].bomb_check():
                neighbor_counter += 1
        self.grid_matrix[row][col].set_neighbors(neighbor_counter)

    def create_board(self):
        self.populate_grid()
        self.plant_bombs()
        for r in xrange(self.row_size):
            #print "loop", r
            for c in xrange(self.col_size):
                #print "loop", c
                self.create_neighbors(r,c) 
                self.calculate_neighbors(r,c)

    def return_bombs(self):
        bomb_matrix = [[False for r in xrange(self.row_size)] for c in xrange(self.col_size)]
        n_matrix = [[False for r in xrange(self.row_size)] for c in xrange(self.col_size)]
        for i  in xrange(self.row_size):
            for j in xrange(self.col_size):
                bomb_matrix[i][j] = self.grid_matrix[i][j].bomb_check()
                n_matrix[i][j] = self.grid_matrix[i][j].get_neighbors()

        return (bomb_matrix, n_matrix)

    def click_cell(self, row, col):
        if self.grid_matrix[row][col].bomb_check():
            #end game
            pass
        self.grid_matrix[row][col].reveal()
        

    def draw_grid(self):
        # displays each cells status
        drawn_grid = []
        for row in xrange(self.row_size):
            drawn_grid.append([])
            for col in xrange(self.col_size):
                cell = self.grid_matrix()
                if cell[row][col].is_flag():
                    draw_grid[row].append("F")        
                elif cell[row][col].is_revealed():
                    drawn_grid[row].append(str(cell[row][col].get_neighbors()))
                else:
                    drawn_grid[row].append("#")

        return drawn_grid

    def get_neighbor_dict(self):
        return self.neighbor_dict


class Game(object):
    def __init__(self):
        pass
    
    def create_game(self, row=8, col=8, bombs=9):
        self.row = row
        self.col = col
        self.bombs = bombs
        self.finished = False
        
        self.grid = Grid()


        self.grid.create_board(row, column)

    def click_cell(self, row, col):
        

    
    def flag_cell(self, row, col):
        pass
    
    def draw_screen(self):
        print "+-"*self.row+"+"
        screen = self.grid.draw_grid()
        for row in self.grid.draw_grid():
            print "|" + "|".join([str(i) if i != 0 else " " for i in row]) + "|"
        print "+-"*self.row+"+"
        self.control()


    def play_game(self):
        while not self.finished:
            pass

            
    def control(self):
        action = raw_input("(C)lick or (F)lag cell?: ").lower()
        if action not in ["f", "c"]:
            "Not a choice."
            return self.control()
        row = raw_input("Which cell row?(Starting at 0): ")
        col = raw_input("Which cell column?(Starting at 0): ")
        if action == "f":
            self.grid.flag_cell(row, col)
        elif action == "c":
            self.grid.click_cell(row, col)




if __name__ == '__main__':
    pass
