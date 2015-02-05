# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 10:56:44 2013
Reads in books.json and extracts selected books

@author: rammanur
"""
import json

with open('notes/books.json') as f:
    catalog = json.load(f)

#print catalog

for key in catalog:
    if catalog[key]['genre'] == 'Computer':
        print catalog[key]['price'], catalog[key]['title']
    