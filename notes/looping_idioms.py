'''Demonstrate Python's preferred looping idioms'''

from itertools import izip

names = 'raymond rachel matthew'.split()
colors = 'red blue yellow green'.split()

for i in range(10):
    print i

for i in xrange(10):
    print i

for name in names:
    print name.capitalize()

for i, name in enumerate(names):
    print i, name.capitalize()

for name, color in zip(names, colors):
    print name, '-->', color

for name, color in izip(names, colors):
    print name, '-->', color

for name in reversed(names):
    print name

for name in sorted(names):
    print name

for name in sorted(names, key=len):
    print name

for name in sorted(names, reverse=True):
    print name

for name in set(names):
    print name

d = dict(izip(names, colors))
for name, color in d.iteritems():
    print name, '-->', color


print '''
GM               Toyota
---              ------
Inventory        JIT Manufacturing
---              --------------
list approach    iterator approach
-------------    -----------
range()          xrange()
zip()            izip()
 --              enumerate()
 --              reversed()
sorted()
set()

d.keys()         d
d.values()       d.itervalues()
d.items()        d.iteritems()

f.readlines()    f

'''
