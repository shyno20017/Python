import sys
import subprocess
import os

firefox = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'

cmd = sys.argv[1]
if cmd == 'openbrowser' or cmd == 'browser':
    ans = input("Enter the url you want to open: ")
    subprocess.call([firefox,'-new-tab', ans])

if cmd == 'openpython' or cmd == 'python':
    os.system('start python')
