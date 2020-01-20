# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 03:58:43 2019

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

    def return_kth_to_last(self, k):
        current = self.head
        stop_num = self.length() - (k-1)
        count = 0
        while current.next != None:
            count = count + 1
            current = current.next
            if count == stop_num:
                return current.data
        
    




my_list = Unsorted_ll()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(10)
my_list.append(40)
my_list.append(50)
my_list.append(20)
my_list.append(10)
my_list.length()
my_list.return_kth_to_last(1)





























