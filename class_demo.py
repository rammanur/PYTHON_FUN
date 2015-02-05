# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 15:02:13 2013

CLASSES DEMO: A simple demo of Python Classes.

@author: rammanur
"""

class Dog:
    "A simple canine class."
    
    def __init__(self, n):
        self.name = n
    
    def __str__(self):
        return "I am a dog named %s" % (self.name,)
        
    def __len__(self):
        return len(self.name)
        
    def __repr__(self):
        return "Dog(%r)" % (self.name,)
    
    def __add__(self, second_dog):
        d = Dog(self.name + second_dog.name)
        return d
        
    def bark(self):
        print "Woof! My name is %s" % (self.name,)
        
        
class Frankendog(Dog):
    def walk(self):
        return "Yes, Dr.Frankenstain"
            
            
