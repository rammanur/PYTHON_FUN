# -*- coding: utf-8 -*-
"""

python kap3.py > kap3.dot
dot -Tsvg kap3.dot -o kap3.svg
open kap3.svg

Analysis of the Kaprekar process.

    >>> kap(495)
    495
    >>> kap(981)
    792
    >>> kap(100)
    099
    >>> kap(990)
    891


"""

def kap3(n):
    "Compute one step of the Kaprekar suite."
    value = "%03d" % n
    big = int("".join(sorted(list(value), reverse=True)))
    little = int("".join(sorted(list(value))))
    return big - little
    
    
def gen_graph():
    kapdict = {}
    for n in range(1000):
        source = "%03d" % n
        target = "%03d" % kap3(n)
        kapdict[source] = target

    list_of_worthy_keys = list(set(kapdict.values()))

    print "digraph {"
    for source in list_of_worthy_keys:
        print "%s -> %s;" % (source, kapdict[source])
    print "}"


if __name__ == '__main__':
    gen_graph()
