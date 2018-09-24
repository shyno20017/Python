from unicurses import *

stdscr = initscr()
k = getch()
while k != ord('q'):
    move(0, 0)
    addstr("You pressed {}".format(k))
    k = getch()
    

endwin()