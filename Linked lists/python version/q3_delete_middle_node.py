# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 03:58:43 2019

@author: Sean Chan
"""

from math import ceil

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

    def delete_middle_node(self):
        middle_num = ceil(self.length() / 2)
        count = 0
        current = self.head
        while current.next != None:
            count = count + 1
            if count == middle_num:
                current.next = current.next.next
                break
            else:
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
my_list.delete_middle_node()
my_list.display()






























