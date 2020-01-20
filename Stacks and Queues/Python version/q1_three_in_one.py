# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:48:09 2019

@author: Sean Chan
"""

class FixedMultiStack:
    def __init__(self, stackSize):
        self.number_of_stacks = 3
        self.stack_capacity = stackSize
        self.values = [0]*(self.stack_capacity * self.number_of_stacks)
        self.sizes = [0]*self.number_of_stacks
    
    def push(self, stackNum, value):
        if isFull(stackNum):
            raise Exception("Stack {} full".format(stackNum))
        else:
            self.sizes[stackNum] = self.sizes[stackNum] + 1
            self.values[indexOfTop(stackNum)] = value
            
    def pop(self, stackNum):
        
    
    
        