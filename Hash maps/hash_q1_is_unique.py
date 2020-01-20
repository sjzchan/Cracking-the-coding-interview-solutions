# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 22:30:56 2019

@author: Sean Chan
"""


setup_code_1 = '''
def is_unique(s):
    
    if len(s) > 128:
        return False
    
    char_set = [0] * 128
    
    for char in s:
        if char_set[ord(char)] == 1:
            return False
        else:
            char_set[ord(char)] = 1
            
    return True
    
s1 = 'qwertyuiopasdfghjklzxcvbnm'
s2 = 'asdfasdf'
'''


setup_code_2 = '''
def is_unique(s):
    if len(s) > 128:
        return False
    
    char_set = set()
    
    for char in s:
        if char in char_set:
            return False
        else:
            char_set.add(char)
    return True

s1 = 'qwertyuiopasdfghjklzxcvbnm'
s2 = 'asdfasdf'
'''

setup_code_3 = '''
def is_unique(s):
    if len(s) > 128:
        return False
    
    char_set = []
    
    for char in s:
        if char in char_set:
            return False
        else:
            char_set.append(char)
    return True
    
s1 = 'qwertyuiopasdfghjklzxcvbnm'
s2 = 'asdfasdf'
'''




import timeit


test_code_1 = '''
is_unique(s1)
'''
test_code_2 = '''
is_unique(s1)
'''
test_code_3 = '''
is_unique(s1)
'''


print(timeit.timeit(setup = setup_code_1,
                    stmt = test_code_1,
                    number = 100000))

print(timeit.timeit(setup = setup_code_2,
                    stmt = test_code_2,
                    number = 100000))

print(timeit.timeit(setup = setup_code_3,
                    stmt = test_code_3,
                    number = 100000))


a = ord('a') - ord('a')
b = ord('b') - ord('a')
c = ord('c') - ord('a')
z = ord('z') - ord('a')

print(1 << a)
print(1 << b)
print(1 << c)
print(1 << z)





