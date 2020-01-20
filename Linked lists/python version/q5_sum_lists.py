# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 04:15:40 2019

@author: Sean Chan
"""

class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

class Unsorted_ll:
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(data)
    
    def display(self):
        elems = []
        current = self.head
        while current.next != None:
            current = current.next
            elems.append(current.data)
        print(elems)

    def length(self):
        count = 0
        current = self.head
        while current.next != None:
            count = count + 1
            current = current.next
        return count

def sum_lists(l1, l2, forward=0):
    current1 = l1.head
    current2 = l2.head
    
    elems1 = []
    elems2 = []
    while current1.next != None:
        current1 = current1.next
        elems1.append(current1.data)
    while current2.next != None:
        current2 = current2.next
        elems2.append(current2.data)
    
    n1 = ''
    n2 = ''
    for i in elems1:
        if forward == 1:
            n1 += str(i)
        else:
            n1 = str(i) + n1
    n1 = int(n1)
    
    for i in elems2:
        if forward == 1:
            n2 += str(i)
        else:
            n2 = str(i) + n2
    n2 = int(n2)
    
    n3 = n1 + n2
    n3 = list(map(int, list(str(n3))))
    
    l3 = Unsorted_ll()
    if forward == 1:
        for i in n3:
            l3.append(i)
    else:
        for i in range(len(n3)-1, -1, -1):
            l3.append(n3[i])
    
    return l3
    


l1 = Unsorted_ll()
l1.append(7)
l1.append(1)
l1.append(6)

l2 = Unsorted_ll()
l2.append(5)
l2.append(9)
l2.append(2)

l1.display()
l2.display()

l3 = sum_lists(l1, l2)
l4 = sum_lists(l1, l2, 1)
l3.display()
l4.display()
















            
            
            
        
            
    