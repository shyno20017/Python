from wrapcurses import Screen, COLOR, KEY, MODIFIER, unicurses

stdscr = Screen()
stdscr.box()
stdscr.set_cursor_position(1, 1)
stdscr.addstr("Hello World!")

window_one = stdscr.create_window(2, 2, 10, 10)
window_one.box()
window_one.addstr("Hello People!", x = 1, y = 1)

window_two = stdscr.create_window(15, 2, 10, 10)
window_two.box()
window_two.addstr("Hello YouTube!", x = 1, y = 1)


stdscr.refresh()
window_one.refresh()
window_two.refresh()

print(stdscr.getmaxyx())
print(window_one.getmaxyx())
print(window_two.getmaxyx())

stdscr.getch()

stdscr.end()
