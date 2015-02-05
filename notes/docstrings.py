'Collection of utilities that use docstrings'

def myhelp(func):
    print 'My Custom Help'
    print '=============='
    print 'Function name:', func.__name__
    print 'Docstring:'
    print func.__doc__

template = '''\
<html>
<head>
<title> Custom HTML Help </title>
</head>
<body>
<h2> Help on function: <em> %s </em> </h2>
<hr>
<pre>
%s
</pre>
</body>
</html>
'''

def myhtmlhelp(func):
    'Emit help() in HTML format'
    print template % (func.__name__, func.__doc__)
    
