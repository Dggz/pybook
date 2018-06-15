import csv

import ipdb; ipdb.set_trace()
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        print(row[0])
        print(row[4])

import ipdb; ipdb.set_trace()
from collections import namedtuple
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        a = row.Symbol
        b = row.Change


import ipdb; ipdb.set_trace()
import json

dat = {'a': True,
     'b': 'Hello',
     'c': None}

with open('fasdfasdfasdaf.json', 'w') as json_f:
    json.dump(dat, json_f)

import ipdb; ipdb.set_trace()
with open('asdf.json', 'r') as f:
    data = json.load(f)
    import ipdb; ipdb.set_trace()
    print()


from xml.etree.ElementTree import parse
with open('fdsa.xml', 'r') as f:
    doc = parse(f)
    import ipdb; ipdb.set_trace()
    print()


from xml.etree.ElementTree import Element
def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

import ipdb; ipdb.set_trace()
s = { 'name': 'GOOG', 'shares': 100, 'price':490.1 }
e = dict_to_xml('stock', s)

import ipdb; ipdb.set_trace()
from xml.etree.ElementTree import tostring
tostring(e)

import ipdb; ipdb.set_trace()
print()
