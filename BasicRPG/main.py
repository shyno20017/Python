from wrapcurses import Screen, Window, COLOR, KEY, MODIFIER
from player import Player

stdscr = Screen()
stdscr.noecho()
stdscr.cursor_set(False)
stdscr.keypad(True)

obj_player = Player(stdscr, "@", COLOR.RED, COLOR.BLACK, MODIFIER.BOLD)

running = True
while running:
    key = stdscr.getch()
    if key == KEY.ESC:
        running = False
        break

    stdscr.clear()
    obj_player.move(key)
    # stdscr.update_all()

stdscr.end()
