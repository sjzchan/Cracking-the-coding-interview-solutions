# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 00:33:44 2019

@author: Sean Chan
"""

def quick_sort(array, left, right):
    index = partition(array, left, right)
    if left < (index-1):
        quick_sort(array, left, index-1)
    if index < right:
        quick_sort(array, index, right)

def partition(array, left, right):
    
    pivot = array[int((left + right) / 2)] # pick pivot point
    
    while left <= right: 
        # find element on left that should be on right
        while array[left] < pivot:
            left = left + 1
            
        # find element on right that should be on left
        while array[right] > pivot:
            right = right - 1
            
        # swap elements, and move left and right indices
        if (left <= right):
            array[left], array[right] = array[right], array[left]
            left = left + 1
            right = right - 1
    
    return left























