# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:31:59 2013

@author: rammanur
"""

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
            