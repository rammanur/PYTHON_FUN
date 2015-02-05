# -*- coding: utf-8 -*-
"""

python kap4.py > kap4.dot
dot -Tsvg kap4.dot -o kap4.svg
open kap4.svg

Analysis of the Kaprekar process.

    >>> kap(6174)
    6174
    >>> kap(12)
    2088
    >>> kap(2088)
    8532
    >>> kap(8532)
    6174

"""

def kap4(n):
    "Compute one step of the Kaprekar suite."
    value = "%04d" % n
    big = int("".join(sorted(list(value), reverse=True)))
    little = int("".join(sorted(list(value))))
    return big - little
    
    
def gen_graph():
    kapdict = {}
    for n in range(10000):
        source = "%04d" % n
        target = "%04d" % kap4(n)
        kapdict[source] = target

    list_of_worthy_keys = list(set(kapdict.values()))

    print "digraph {"
    for source in list_of_worthy_keys:
        print "%s -> %s;" % (source, kapdict[source])
    print "}"


if __name__ == '__main__':
    gen_graph()
