# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 23:25:45 2019

@author: Sean Chan
"""


def URLify_x(s):
    for i in range(len(s)):
        if s[i] != ' ':
            s = s[i:]
            break
    for i in range(len(s)-1, 0, -1):
        if s[i] != ' ':
            s = s[0:i+1]
            break
    
    url = ''
    last_idx = 0
    for i in range(len(s)):
        if s[i] == ' ':
            url += s[last_idx:i]
            last_idx = i+1
            url += '%20'
        if i == len(s)-1:
            url += s[last_idx:]

    return url


def URLify(s):
    url = ''
    for i in range(len(s)):
        if s[i] == ' ':
            url += '%20'
        else:
            url += s[i]
    return url            
    


s = 'a s f g e fds ferghgfgfdfads fd'
print(URLify(s))




