# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:43:12 2019

@author: Sean Chan
"""

class Stack:
    class Node:
        def __init__(self, data=0):
            self.data = data
            self.prev = None
    
    def __init__(self):
        self.top = None
    
    def sortStack(self):
        
    
    
    def push(self, data):
        if self.top == None:
            self.top = self.Node(data)
        else:
            newNode = self.Node(data)
            newNode.prev = self.top
            self.top = newNode
    
    def pop(self):
        self.top = self.top.prev
    
    def peek(self):
        return self.top.data
    
    def isEmpty(self):
        return self.top == None
    
    def display(self):
        elems = []
        current = self.top
        while current != None:
            elems.append(current.data)
            current = current.prev
        print(elems)

s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.display()    
    
    
    