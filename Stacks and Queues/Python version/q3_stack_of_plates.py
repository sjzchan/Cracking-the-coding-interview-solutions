# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:54:21 2019

@author: Sean Chan
"""

class SetOfStacks:
    class Stack:        
        class Node:
            def __init__(self, data=0):
                self.data = data
                self.prev = None
                
        def __init__(self):
            self.top = None
            self.height = 0
            self.prev_stack = None
        
        def push(self, data):
            current = self.top
            if current == None:
                self.top = self.Node(data)
            else:
                newNode = self.Node(data)
                newNode.prev = current
                self.top = newNode
            self.height = self.height + 1
            
        def pop(self):
            current = self.top
            self.top = current.prev
            self.height = self.height - 1
    
        def display(self):
            elems = []
            current = self.top
            while current != None:
                elems.append(current.data)
                current = current.prev
            print(elems)
            
        
    def __init__(self, threshold=3):
        self.threshold = threshold
        self.current_stack = self.Stack()
        self.num_stacks = 1
        
    def getNewStack(self):
        newStack = self.Stack()
        current = self.current_stack
        newStack.prev_stack = current
        self.current_stack = newStack
        self.num_stacks = self.num_stacks + 1
        
    def push(self, data):
        if self.current_stack.height == self.threshold:
            self.getNewStack()
        self.current_stack.push(data)
        
    def pop(self):
        if self.current_stack.height == 0:
            self.current_stack = self.current_stack.prev_stack
        self.current_stack.pop()
    
    def popAt(self, subStack):
        curr_subStack = self.num_stacks
        current = self.current_stack
        while(curr_subStack != subStack):
            current = current.prev_stack
            curr_subStack = curr_subStack - 1
        current.pop()
        
    def display(self):
        current = self.current_stack
        while current != None:
            current.display()
            current = current.prev_stack
    
    def display_heights(self):
        current = self.current_stack
        while current != None:
            print(current.height)
            current = current.prev_stack
        
        
ss1 = SetOfStacks()
ss1.push(10)
ss1.push(10)
ss1.push(10)
ss1.push(20)
ss1.push(20)
ss1.push(20)
ss1.push(30)
ss1.push(30)
ss1.push(30)
ss1.display()
ss1.popAt(1)
ss1.pop()
ss1.pop()
ss1.pop()
ss1.pop()
ss1.pop()
ss1.display()
ss1.display_heights()




