# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 21:04:59 2013

@author: rammanur
"""

# Iterating over lists

def count_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 1:
            count += 1
    return count

def check_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            return True
    return False

def remove_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            numbers.remove(num)

def remove_odd2(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(numbers.index(num))
            
    for idx in remove:
        numbers.pop(idx)
        
def remove_odd3(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(num)
            
    for num in remove:
        numbers.remove(num)
        
def remove_odd4(numbers):
    newnums = []
    for num in numbers:
        if num % 2 == 0:
            newnums.append(num)
    return newnums
   
def remove_last_odd(numbers):
    has_odd = False
    last_odd = 0
    for num in numbers:
        if num % 2 == 1:
            has_odd = True
            last_odd = numbers.index(num)
            print "last_odd is %d num=%d" % (last_odd, num)
            
    """if has_odd:
        numbers.remove(last_odd)"""
        
def square_list1(numbers):
    """Returns a list of the squares of the numbers in the input."""
    result = []
    for n in numbers:
        result.append(n ** 2)
    return result

def square_list2(numbers):
    """Returns a list of the squares of the numbers in the input."""
    return [n ** 2 for n in numbers]

print square_list1([4, 5, -2])
print square_list2([4, 5, -2])



def is_in_range(ball):
    """Returns whether the ball is in the desired range.  """
    return ball[0] >= 0 and ball[0] <= 100 and ball[1] >= 0 and ball[1] <= 100


def balls_in_range1(balls):
    """Returns a list of those input balls that are within the desired range."""
    result = []
    for ball in balls:
        if is_in_range(ball):
            result.append(ball)
    return result

def balls_in_range2(balls):
    return [ball for ball in balls if is_in_range(ball)]

print balls_in_range1([[-5,40], [30,20], [70,140], [60,50]])
print balls_in_range2([[-5,40], [30,20], [70,140], [60,50]])

def run():
    numbers = [1, 7, 2, 34, 8, 7, 2, 5, 14, 22, 93, 48, 76, 15, 7]
    print numbers
    remove_last_odd(numbers)
    print numbers
    
run()

