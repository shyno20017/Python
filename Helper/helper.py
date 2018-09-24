import keyboard
import os

def open_python():
    os.system("start python")

def run_cmd():
    os.system("start python cmd.py")

def run_browse(cmd):
    os.system("start python browse.py " + cmd)

keyboard.add_hotkey('o, p, e, n, b, r, o, w, s, e, r', run_browse, ['browser'])

keyboard.add_hotkey('o, p, e, n, p, y, t, h, o, n', open_python)

keyboard.add_hotkey('r, u, n, c, m, d', run_cmd)

keyboard.add_hotkey('g, o, o, g, l, e, s, e, a, r, c, h', run_browse, ['google'])

keyboard.add_hotkey('y, o, u, t, u, b, e, s, e, a, r, c, h', run_browse, ['youtube'])

keyboard.add_hotkey('o, p, e, n, a, t, o, m', run_browse, ['atom'])

keyboard.add_hotkey('s, a, y, h, i', run_browse, ['hi'])

keyboard.add_hotkey('p, l, a, y, t, e, r, r, a, r, i, a', run_browse, ['terraria'])

keyboard.add_hotkey('p, l, a, y, m, o, d, d, e, d', run_browse, ['modded'])

keyboard.add_hotkey('s, h, o, w, i, p', run_browse, ['ipconfig'])

keyboard.wait('c, l, o, s, e, h, e, l, p, e, r')
