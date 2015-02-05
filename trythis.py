# Search a directory tree for all files with duplicate content

import os, hashlib, pprint

hashmap = {} # content signature -> list of matching filenames

import signal

def print_linenum(signum, frame):
    print "Currently at line", frame.f_lineno

signal.signal(signal.SIGINT, print_linenum)

for path, dirs, files in os.walk('.'):
    for filename in files:
        fullname = os.path.join(path, filename)
        d = open(fullname).read()
        h = hashlib.md5(d).hexdigest()
        hashmap.setdefault(h, []).append(fullname)

pprint.pprint(hashmap)
