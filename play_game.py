from pysweeper import Cell, Grid, Game
# import curses
# import curses.textpad
# import time

#print "Pres"
'''
rows = raw_input("How many rows would you like? (Press enter for 8) ")
cols = raw_input("How many columns would you like? (Press enter for 8) ")
bombs = raw_input("How many bombs would you like? (Press enter for 9) ")

print type(rows)
print cols
print bombs
''' 

game = Game()
game.create_game()

#n_dict = grid.get_neighbor_dict()

#game.draw_screen()
game.play_game()

#window = curses.initscr()
#curses.endwin()


