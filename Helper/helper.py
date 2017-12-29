import keyboard
import os

def open_browser(cmd):
    os.system("start python browse.py " + cmd)

def open_python():
    os.system("start python")

def run_cmd():
    os.system("start python cmd.py")

keyboard.add_hotkey('o, p, e, n, b, r, o, w, s, e, r', open_browser, ['browser'])

keyboard.add_hotkey('o, p, e, n, p, y, t, h, o, n', open_python)

keyboard.add_hotkey('r, u, n, c, m, d', run_cmd)

keyboard.wait('c, l, o, s, e, h, e, l, p, e, r')
