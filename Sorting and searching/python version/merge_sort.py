# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 00:05:38 2019

@author: Sean Chan
"""

def merge_sort(array):
    helper = array
    merge_sort2(array, helper, 0, len(array)-1)
    
def merge_sort2(array, helper, low, high):
    if low < high:
        middle = (low + high) / 2
        merge_sort2(array, helper, low, middle) # sorts left half
        merge_sort2(array, helper, middle+1, high) # sorts right half
        merge(array, helper, low, middle, high) # merge them

def merge(array, helper, low, middle, high):
    for i in range(low, high): # copy both halves into a helper array
        helper[i] = array[i]
    
    helperLeft = low
    helperRight = middle+1
    current = low
    
    # iterate through the helper array. Compare the left and right
    # half, copying back the smaller element from the two halves 
    # into the original array
    while helperLeft <= middle and helperRight <= high:
        if helper[helperLeft] <= helper[helperRight]:
            array[current] = helper[helperLeft]
            helperLeft = helperLeft + 1
        else:
            array[current] = helper[helperRight]
            helperRight = helperRight + 1
        current = current + 1
    
    remaining = middle - helperLeft
    for i in range(remaining + 1):
        array[current + i] = helper[helperLeft + i]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    