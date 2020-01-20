# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 22:56:48 2019

@author: Sean Chan
"""



class Stack():
    class Node():
        def __init__(self, data=0):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.top = None
        self.min_element = None
    
    def push(self, data):
        if self.top == None:
            self.top = self.Node(data)
        else:
            newNode = self.Node(data)
            newNode.next = self.top
            self.top = newNode
        if self.top.data < self.min_element:
            self.min_element = self.top.data
        
    
    def pop(self):
        self.elements.remove(self.top.data)
        self.top = self.top.next

    def peek(self):
        return self.top.data
    
    def isEmpty(self):
        return self.top == None
    
    def display(self):
        elems = []
        current = self.top
        while (current != None):
            elems.append(current.data)
            current = current.next
        print(elems)
    


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.peek()
s1.display()
s1.pop()
s1.pop()
s1.display()
s1.isEmpty()
s1.pop()
s1.display()
s1.isEmpty()








