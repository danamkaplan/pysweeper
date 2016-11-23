from pysweeper import Cell, Grid
import curses
import curses.textpad
import time

print "Welcome to the first game of the rest of your life"
#print "Pres"
'''
rows = raw_input("How many rows would you like? (Press enter for 8) ")
cols = raw_input("How many columns would you like? (Press enter for 8) ")
bombs = raw_input("How many bombs would you like? (Press enter for 9) ")

print type(rows)
print cols
print bombs
''' 

grid = Grid()
grid.create_board()

grid.return_bombs()

window = curses.initscr()
curses.endwin()


