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

bombs, neighbors = grid.return_bombs()

n_dict = grid.get_neighbor_dict()

''' 
for i, j in n_dict.iteritems():
    print i, j
'''
#for i in bombs:
#    print i
#print "---------"

for j in neighbors:
    print "+-"*8+"+"
    print "|" + "|".join([str(i) for i in j]) + "|"
    
print "+-"*8+"+"
window = curses.initscr()
curses.endwin()


