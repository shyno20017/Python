import sys
import subprocess
import os

firefox = r'C:\Program Files\Mozilla Firefox\firefox.exe'

cmd = sys.argv[1]
if cmd == 'openbrowser' or cmd == 'browser':
    ans = raw_input("Enter the url you want to open: ")
    subprocess.call([firefox,'-new-tab', ans], shell=True)

if cmd == 'openpython' or cmd == 'python':
    os.system('start python')
