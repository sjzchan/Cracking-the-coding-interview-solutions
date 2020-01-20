# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 05:04:47 2019

@author: Sean Chan
"""

        
        


x = 10
y = 10
z = x

print(id(x))
print(id(y))
print(id(z))

x += 10

print(x, id(x))
print(y, id(y))
print(z, id(z))
            
            
            