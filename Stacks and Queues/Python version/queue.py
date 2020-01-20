# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:42:21 2019

@author: Sean Chan
"""

class Queue():
    class Node():
        def __init__(self, data=0):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.head = None
        self.tail = self.head
    
    def add(self, data):
        if self.head == None:
            self.head = self.Node(data)
            self.tail = self.head
        else:
            newNode = self.Node(data)
            current = self.tail
            current.next = newNode
            self.tail = newNode
    
    def remove(self):
        self.head = self.head.next
    
    def peek(self):
        return self.head.data
    
    def isEmpty(self):
        return self.head == None
    
    def display(self):
        elems = []
        current = self.head
        while current != None:
            elems.append(current.data)
            current = current.next
        print(elems)
    
q1 = Queue()
q1.add(10)
q1.add(20)
q1.display()
q1.remove()
q1.display()
        
        
        
        
        
        
        
        
        