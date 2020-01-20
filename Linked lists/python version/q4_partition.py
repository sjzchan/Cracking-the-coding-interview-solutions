# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 04:15:40 2019

@author: Sean Chan
"""

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

    def partition(self, x):
        greater = Unsorted_ll()
        current = self.head
        current_greater = greater.head
            
        while current.next != None:
            if current.next.data >= x:
                current_greater.next = Node(current.next.data)
                current_greater = current_greater.next
                current.next = current.next.next
            else:
                current = current.next
                
        current.next = greater.head.next
    

my_list = Unsorted_ll()
my_list.append(10)
my_list.append(40)
my_list.append(50)
my_list.append(20)
my_list.append(30)
my_list.append(10)
my_list.append(20)
my_list.append(10)
my_list.display()
my_list.partition(30)
my_list.display()
















            
            
            
        
            
    