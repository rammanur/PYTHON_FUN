'Complete analysis of the Kaprekar Process'
#http://en.wikipedia.org/wiki/6174_(number)

def kap(n):
    '''Compute one-step of the Kaprekar Process

        >>> kap(3524)
        3087
        >>> kap(3087)
        8352
        >>> kap(8352)
        6174
        >>> kap(6174)
        6174

    '''
    s = '%04d' % n
    small = int(''.join(sorted(s)))
    big = int(''.join(sorted(s, reverse=True)))
    return big - small

def gen_graph():
    ''' Graphically analyze the kap() function
        is graphviz format (also known as dot).

        To build the graph, run this at the command-line:

            $ python kap.py | dot -Tsvg > kap.svg

    '''
    
    # Step 1:  Convert data to a convenient form
    kapdict = {}
    for i in range(10000):
        tgt = kap(i)
        kapdict['%04d' % i] = '%04d' % tgt

    # Step 2:  Analyze the data
    firsts = set(kapdict.keys()) - set(kapdict.values())
    rest = set(kapdict.keys()) - firsts
    assert len(firsts) + len(rest) == len(kapdict)

    groups = {}
    for i in sorted(firsts):
        tgt = kapdict[i]
        groups.setdefault(tgt, []).append(i)

    # Step 3:  Format the output

    print '''\
    digraph {
    graph [rankdir=LR, label="Kaprekar Process", labelloc=t, fontsize=48];
    edge [color=blue, fontsize=10, fontcolor=blue];
    '''

    for i in sorted(rest):
        tgt = kapdict[i]
        print '%s -> %s;' % (i, tgt)

    print 'node [shape=rectangle];'

    for tgt, group in sorted(groups.items()):
        block = ', '.join(group[:3])
        print '"%s, ..." -> %s [label=%d];' \
              % (block, tgt, len(group))

    print '}'


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    gen_graph()
