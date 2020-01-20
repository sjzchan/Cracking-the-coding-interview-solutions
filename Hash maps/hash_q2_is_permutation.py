# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 16:55:59 2019

@author: Sean Chan
"""


def is_permutation(s1, s2):
    
    if len(s1) != len(s2):
        return False
    else:
        d = {}
        for c1 in s1:
            if c1 in d.keys():
                d[c1] += 1
            else:
                d[c1] = 1
    
        for c2 in s2:
            if c2 not in d.keys():
                return False
            else:
                d[c2] -= 1
        
        if all(value == 0 for value in d.values()):
            return True
        

s1 = 'asdfasdf'
s2 = s1[::-1]
s3 = 'qwerqwer'

print(is_permutation(s1, s2))
print(is_permutation(s1, s3))


