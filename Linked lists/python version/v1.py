# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:38:37 2019

@author: Sean Chan
"""


class Node:
    def __init__(self, data=None):
        self.next = None;
        self.data = data;
    
    
class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        current = self.head
        if current == None:
            current = Node(data)
        else:
            while current.next != None:
                current = current.next
            current.next = Node(data)
        
    def printLL(self):
        elems = []
        current = self.head
        while current.next != None:
            current = current.next
            elems.append(current.data)
        print(elems)
    
    
            

    
LL = LinkedList()
LL.append(10)
LL.append(20)
LL.append(30)

LL.printLL()


