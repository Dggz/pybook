#
#   Definitely the first 3 things
#


# https://web.archive.org/web/20170628162655/http://chimera.labs.oreilly.com:80/books/1230000000393/ch13.html#_solution_223
# filein.py
import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')

### don't pass over this
# --- Terminating with err msg
# raise SystemExit('It failed!')  # better than the next code block

# import sys
# sys.stderr.write('It failed!\n')
# raise SystemExit(1)
### don't pass over this

#
#
# --- argparse, show nts maybe
#
#
# parser.add_argument('--speed', dest='speed', action='store',
#                     choices={'slow','fast'}, default='slow',
#                     help='search speed')
# Show alternative to this
#

import getpass

from cripto.belaso import belasso_decrypt

# parolafoartesigura
pwds = {'cbaciu': 'JJUPND XDSVHMRJVTD'}

def svc_login(user, passwd):
    if passwd == belasso_decrypt(pwds[user], user[::-1]):
        return True
    return False

user = getpass.getuser()
passwd = getpass.getpass()

if svc_login(user, passwd):    # You must write svc_login()
   print("Yay!")
else:
   print("Syke, that's the wrong password!")


# ---
# Terminal size

import os
sz = os.get_terminal_size()

# ---
# External commands

import subprocess
out_bytes = subprocess.check_output(['ls','-la'])
out_text = out_bytes.decode('utf-8')


# ---
# Countdown timer

import time

class Timer:
    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self._func()
        self.elapsed += end - self._start
        self._start = None

    def reset(self):
        self.elapsed = 0.0

    @property
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()

def countdown(n):
    while n > 0:
        n -= 1

# Use 1: Explicit start/stop
t = Timer()
t.start()
countdown(1000000)
t.stop()
print(t.elapsed)

# Use 2: As a context manager
with t:
    countdown(1000000)
print(t.elapsed)

with Timer() as t2:
    countdown(1000000)
print(t2.elapsed)


# ---
# Open webbrowser
import webbrowser


webbrowser.open('http://www.python.org')
webbrowser.open_new('http://www.python.org')
webbrowser.open_new_tab('http://www.python.org')

c = webbrowser.get('firefox')
c.open('http://www.python.org')
c.open_new_tab('http://docs.python.org')
