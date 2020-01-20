# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 04:28:51 2019

@author: Sean Chan
"""

from math import floor, ceil
from queue import LifoQueue as Stack

class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

class Unsorted_ll:
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(data)
    
    def display(self):
        elems = []
        current = self.head
        while current.next != None:
            current = current.next
            elems.append(current.data)
        print(elems)

    def length(self):
        count = 0
        current = self.head
        while current.next != None:
            count = count + 1
            current = current.next
        return count
    
    def is_palindrome(self):
        first_half = Stack()
        current = self.head
        half_len = self.length() / 2
        count = 0
        if floor(half_len) == ceil(half_len):
            middle = False
            half_len = ceil(half_len)
        else:
            middle = True
            half_len = ceil(half_len) - 1
        
        while current.next != None:
            current = current.next
            count = count + 1
            first_half.put(current.data)
            if count == half_len:
                break
        
        if middle == True:
            current = current.next
            
        while current.next != None:
            current = current.next
            if current.data != first_half.get():
                return False
        
        return True
            
    
    
    
l1 = Unsorted_ll()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(20)
l1.append(20)
l1.display()
l1.is_palindrome()

l2 = Unsorted_ll()
l2.append(10)
l2.append(20)
l2.append(20)
l2.append(20)
l2.display()
l2.is_palindrome()

    
    
    
    
    
    
    
    
    
    
    