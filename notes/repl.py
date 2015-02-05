# Custom REPL for Python

In = []
Out = []

while True:
    prompt = 'In [%d]: ' % len(In)
    request = raw_input(prompt)

    # custom commands
    if request == 'quit':
        break
    if request.startswith('?'):
        function = request[1:]
        help(function)
        continue
        
    
    result = eval(request)
    print 'Out[%d]: %s\n' %(len(Out), repr(result))

    In.append(request)
    Out.append(result)
