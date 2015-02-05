# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:24:56 2013

TEST DRIVEN DEVELOPMENT (TDD):
Unit-test module for Dictionary.

@author: rammanur
"""

import unittest #TL.DR
from utilities import Dict

class TestDictionaryFunctions(unittest.TestCase):
    def test_basic(self):
        d = Dict()
        d['raymond'] = 'red'
        d['rachel'] = 'blue'
        d['matthew'] = 'green'
        self.assertEqual(d['raymond'], 'red')
        self.assertEqual(d['rachel'], 'blue')
        self.assertEqual(d['matthew'], 'green')

    def test_delete_key(self):
        d = Dict()
        d['raymond'] = 'red'
        del d['raymond']
        with self.assertRaises(KeyError):
            d['raymond']
        
    def test_get_keys(self):
        d = Dict()
        d['raymond'] = 'red'
        d['rachel'] = 'blue'
        d['matthew'] = 'green'
        self.assertEqual(sorted(d.keys()), 
                         sorted(['raymond', 'rachel', 'matthew']))

    def test_use_get(self):
        d = Dict()
        d['raymond'] = 'red'
        self.assertEqual(d.get('raymond'), 'red')
        self.assertEqual(d.get('rachel'), None)
        self.assertEqual(d.get('rachel', 'blank'), 'blank')

        
    def test_get_values(self):
        d = Dict()
        d['raymond'] = 'red'
        d['rachel'] = 'blue'
        d['matthew'] = 'green'
        self.assertEqual(sorted(d.values()), 
                         sorted(['red', 'blue', 'green']))

    def test_use_setdefault(self):
        d = Dict()
        d['raymond'] = 'red'
        self.assertEqual(d.setdefault('raymond'), 'red')
        self.assertEqual(d.setdefault('rachel'), None)
        self.assertEqual(d.setdefault('rachel', 'blank'), None)
        self.assertEqual(d.setdefault('matthew', 'green'), 'green')

    def test_in(self):
        d = Dict()
        d['raymond'] = 'red'
        self.assertEqual('raymond' in d, True)
        self.assertEqual('rachel' in d, False)

if __name__ == '__main__':
    unittest.main(exit=False)