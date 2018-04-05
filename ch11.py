
from urllib import request, parse

# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
   'name1' : 'value1',
   'name2' : 'value2'
}

# Encode the query string
querystring = parse.urlencode(parms)

# Extra headers
headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}

req = request.Request(url, querystring.encode('ascii'), headers=headers)

# Make a request and read the response
u = request.urlopen(req)
resp = u.read()



import requests  # needs to be installed, third-party

# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
   'name1' : 'value1',
   'name2' : 'value2'
}

# Extra headers
headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}

resp = requests.post(url, data=parms, headers=headers)

# Decoded text returned by the request
text = resp.text
jss = resp.json()

#####################

import requests

resp = requests.head('http://www.python.org/index.html')

status = resp.status_code
resp.headers


# Talk between interpreters


# Server
from multiprocessing.connection import Listener
import traceback

def echo_client(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
    except EOFError:
        print('Connection closed')

def echo_server(address, authkey):
    serv = Listener(address, authkey=authkey)
    while True:
        try:
            client = serv.accept()
            echo_client(client)
        except Exception:
            traceback.print_exc()

echo_server(('', 25000), authkey=b'peekaboo')

# Client

from multiprocessing.connection import Client
c = Client(('localhost', 25000), authkey=b'peekaboo')
c.send('hello')
c.recv()


"""
Avantaje: mesajele raman intacte (serializate cu pickle)

As a general rule, you would not be using multiprocessing to implement 
public-facing services. The authkey parameter to Client() and Listener() is 
there to help authenticate the end points of the connection. Connection attempts
with a bad key raise an exception. In addition, the module is probably best 
suited for long-running connections (not a large number of short connections). 
For example, two interpreters might establish a connection at startup and 
keep the connection active for the entire duration of a problem.

"""

"""Remote procedure calls"""

# https://web.archive.org/web/20170716103846/http://chimera.labs.oreilly.com:80/books/1230000000393/ch11.html#_problem_191

"""Insecure"""
"""Use the files"""











