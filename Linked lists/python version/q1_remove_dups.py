# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 01:45:53 2019

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
        
    
    def remove_dups(self):
        members = set()
        current = self.head
        while current.next != None:
            if current.next.data in members:
                current.next = current.next.next
            else:
                members.add(current.next.data)
                current = current.next
                
                

my_list = Unsorted_ll()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(10)
my_list.append(40)
my_list.append(50)
my_list.append(20)
my_list.append(10)
my_list.display()
my_list.remove_dups()
my_list.display()


