
#
#   Definitely the first 3 things
#



# https://web.archive.org/web/20170628162655/http://chimera.labs.oreilly.com:80/books/1230000000393/ch13.html#_solution_223
# filein.py
import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')

# --- Terminating with err msg
# raise SystemExit('It failed!')  # better than the next code block

# import sys
# sys.stderr.write('It failed!\n')
# raise SystemExit(1)


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

def svc_login():
    print('Do this with RSA encryption')
    return True

user = getpass.getuser()
passwd = getpass.getpass()

if svc_login(user, passwd):    # You must write svc_login()
   print('Yay!')
else:
   print('Boo!')

