#!/bin/python

from __future__ import unicode_literals 
import sys
import os
import re
import argparse


sizes = {
    'b': 1,
    'k': 1000,
    'm': 1000000,
    'g': 1000000000,
    't': 1000000000000,
}

size_pattern = "\d+\s"


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('filename',  type=str,
                   help='file to create')
parser.add_argument('size',  type=str,
                  help='Size of file to create. Express in [b, k, m, g, t]. Example: 100m for 100 megabytes.')
parser.add_argument('-f', help='Make it happen', action='store_true')
args = parser.parse_args()


m = re.match('(?P<number>\d+)(?P<magnitude>\w)', args.size.lower())
groupdict = m.groupdict()
if not sizes.get(groupdict.get('magnitude')) or not groupdict.get('number'):
    print('Invalid size.')
    sys.exit(1)

total_size = int(groupdict.get('number')) * sizes.get(groupdict.get('magnitude'))

if os.path.exists(args.filename) and not args.f:
    print('file %s exists, use -f if you want to overwrite.' % args.filename)
    sys.exit(2)

with open(args.filename, 'w') as f:
    f.write('0' * total_size)
        
