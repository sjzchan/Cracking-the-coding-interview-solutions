# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 01:02:43 2019

@author: Sean Chan
"""

def is_palindrome_perm(s):
    
    s = s.lower()
    
    d = {}
    
    for c in s:
        if c == ' ':
            continue
        else:
            if c in d.keys():
                d[c] += 1
            else:
                d[c] = 1
    
    num_one = 0
    for i in d.values():
        if i == 1:
            if num_one == 1:
                return False
            else:
                num_one += 1
        elif i != 2:
            return False
        else:
            continue
    return True




s = "Tact Coa"

print(is_palindrome_perm(s))
