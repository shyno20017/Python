import sys
import subprocess
import os

<<<<<<< HEAD
firefox = r'C:\Program Files\Mozilla Firefox\firefox.exe'
=======
firefox = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
editor = r'C:\Users\Mohamed\AppData\Local\atom\atom.exe'
terraria = r"C:\Users\Mohamed\Desktop\Games\Omar's Games\Terraria\Terraria.exe"
modded = r"C:\Users\Mohamed\Desktop\Games\Omar's Games\Terraria\Terraria (2).exe"
>>>>>>> cc2ab36aac1a071571c4dd9d44cb4a541b5f7c65

cmd = sys.argv[1]
if cmd == 'openbrowser' or cmd == 'browser':
    ans = raw_input("Enter the url you want to open: ")
    subprocess.call([firefox,'-new-tab', ans], shell=True)

if cmd == 'openpython' or cmd == 'python':
    os.system('start python')


if cmd == 'google' or cmd == 'search':
    ans = input("What would you like to google search: ").replace(' ', '+')
    query = 'http://www.google.com/search?q=' + ans
    subprocess.call([firefox,'-new-tab', query])


if cmd == 'youtube':
    ans = input("What would you like to search on youtube: ").replace(' ', '+')
    query = 'https://www.youtube.com/results?search_query=' + ans
    subprocess.call([firefox,'-new-tab', query])


if cmd == 'atom':
    subprocess.call([editor])

if cmd == 'terraria':
    subprocess.call([terraria])

if cmd == 'modded':
    subprocess.call([modded])


if cmd == 'hi':
    print("Welome to the Helper Bots Center:")
    ans = input("May I help you? ")
    while ans != '' and ans != 'close' and ans != 'exit':
        if ans == 'help':
            print("Here is a list of commands:")
            print("Help: prints this help screen")
            print("openbrowser: opens a new browser to the url specified")
            print("openpython: opens a new window with python running")
            print("googlesearch: opens a new browser tab with google results to search query")
            print("youtubesearch: opens a new browser tab with youtube results to search query")
            print()

        ans = input("Any further commands? ")


if cmd == 'ipconfig' or cmd == 'ip':
    os.system('ipconfig')
    input()
