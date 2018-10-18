from wrapcurses import COLOR, KEY

class Player:
    def __init__(self, stdscr, body: str, foreground: int = None, background: int = None, attributes: int = 0):
        self.max_x = stdscr.width - 1
        self.max_y = stdscr.height - 1

        self.x = self.max_x // 2
        self.y = self.max_y // 2
        self.body = body

        # Create the player
        self.window = stdscr.create_window(self.x, self.y, 1, 1)

        self.foreground = foreground
        self.background = background
        self.color = 0

        self.attributes = attributes

        self.window.bkgd(self.body, self.attributes)

        if foreground is not None and background is not None:
            self.set_colors(foreground, background)

        self.show_changes()

    def set_colors(self, foreground, background):
        self.color = COLOR.create_color(foreground, background)

        self.foreground = foreground
        self.background = background

        self.window.bkgd(self.body, self.attributes + self.color)
        self.show_changes()

    def move(self, key, motion = 1):
        moved = False

        if key == KEY.UP_KEY:
            if not (self.y - motion < 0):
                moved = True
                self.y -= motion
        elif key == KEY.DOWN_KEY:
            if not (self.y + motion > self.max_y):
                moved = True
                self.y += motion
        elif key == KEY.LEFT_KEY:
            if not (self.x - motion < 0):
                moved = True
                self.x -= motion
        elif key == KEY.RIGHT_KEY:
            print(self.x)
            if not (self.x + motion > self.max_x):
                moved = True
                self.x += motion

        self.window.move(self.x, self.y)
        self.show_changes()

    def show_changes(self):
        self.window.update_all()
