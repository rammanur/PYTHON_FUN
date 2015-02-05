# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 10:14:40 2013

Bunch of utility classes to be used for other Py Apps

@author: rammanur

"""

def REPL():
    "Read–eval–print loop: A read–eval–print loop (REPL) is a simple, \
    interactive computer programming environment. The term is most usually used\
    to refer to a Lisp interactive environment, but can be applied to command \
    line shells and similar environments for programming languages such as APL,\
    BASIC, Clojure, F'#', Haskell, J, Julia, Perl, PHP, Prolog, Python, R,\
    Ruby, Scala, Smalltalk, Standard ML, Tcl, Javascript, et al. Synonyms \
    include interactive toplevel and language shell."
    
    In = [None]
    Out = [None]
    count = 0
    while True:
        count += 1
        try:
            command = raw_input("In [%d]: " % (count,))
            In.append(command)
            result = eval(command)
            Out.append(result)
            print "Out[%d]: %r" % (count, result)

        except EOFError:
            print "\nExiting REPL"
            return
        except SyntaxError:
            print "SyntaxError: unexpected EOF while parsing. TRY AGAIN!"
            count -= 1
        except NameError: 
            print "NameError: name \'%s\' is not defined" % (command,)
            count -= 1


class Dict():
    "Improved implementation of Python's dict."
    
    def __init__(self):
        self.size = 8;
        self.desks = [ [] for i in range(self.size) ]
        self.folders = [ [] for i in range(self.size) ]

    def __setitem__(self, key, value):
        "Implements d[key] = value."
        
        position = abs(hash(key)) % self.size
        desk = self.desks[position]
        folder = self.folders[position]
        if key in desk:
            j = desk.index(key)
            folder[j] = value
        else:
            desk.append(key)
            folder.append(value)
            
    def __getitem__(self, key):
        "Implements gettingvalue via d[key]."
        position = abs(hash(key)) % self.size
        desk = self.desks[position]
        folder = self.folders[position]
        try:
            j = desk.index(key)
        except ValueError:
            raise KeyError    
        
        return folder[j]
            
    def __delitem__(self, key):
        "Implements deleting an item for given key"
        try:
            position = abs(hash(key)) % self.size
            desk = self.desks[position]
            j = desk.index(key)
            folder = self.folders[position]
            del folder[j]
            del desk[j]
        except ValueError:
            raise KeyError    
      
    def __iter__(self):
        "Reminder that desks looks like  [ [], [], [], ... ]"
        for desk in self.desks:
            for key in desk:
                yield key
                
    def keys(self):
        "Returns list of keys in Dict."
        #all_keys = []
        #for desk in self.desks:
            #all_keys.extend(desk)
        #return all_keys
        return list(self)

    def get(self, key, default_value=None):
        "Returns d.get(k,d)"
        try:
            value = self[key] 
        except KeyError:
            value = default_value
        return value
            
    def values(self):
        "Returns list of values in Dict."
        return [ self[key] for key in self ]

    def setdefault(self, key, default_value=None):
        "Returns d.setdefault(k, [d])."
        try:
            value = self[key]
        except KeyError:
            self[key] = default_value
            value = default_value
        return value


def file_value_counter(filename):
    #holdings, count = [], 0
    total_sum, count = 0, 0
    with open(filename) as f:
        for line in f:
            values = line.strip()
            if [ values != '']:
                #print "%s" % values
                #holdings.append(float(values))
                total_sum += float(values)
            count += 1
    f.close()
    return total_sum, count
    
def add_dollar_amounts(filename):
    total_sum, line_entries = 0, 0
    with open(filename) as f:
        for line in f:
            values = line.strip().replace(',', "").strip("$")
            total_sum += float(values)
            line_entries += 1
    f.close()
    return total_sum, line_entries


if __name__ == '__main__':
    REPL()
