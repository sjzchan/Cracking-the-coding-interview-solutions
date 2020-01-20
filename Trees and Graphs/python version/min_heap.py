

"""
Mappings:
    Parent -> int((childIndex - 1) / 2)
    Left Child -> 2 * parentIndex + 1
    Right Child -> 2 * parentIndex + 2
"""


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def peek(self):
        if not self.heap:
            return self.heap[0]
        else:
            return "Heap is empty"
    
    def getLeftChildIndex(self, parentIndex):
        return int(2 * parentIndex + 1)
    
    def getRightChildIndex(self, parentIndex):
        return int(2 * parentIndex + 2)
    
    def getParentIndex(self, childIndex):
        return int((childIndex - 1) / 2)
    
    def hasLeftChild(self, parentIndex):
        return self.getLeftChildIndex < self.size
    
    def hasRightChild(self, parentIndex):
        return self.getRightChildIndex < self.size
    
    def hasParent(self, childIndex):
        return (childIndex != 0) and getParentIndex(childIndex) >= 0
    
    def leftChild(self, parentIndex):
        return self.heap[self.getLeftChildIndex(parentIndex)]
    
    def rightChild(self, parentIndex):
        return self.heap[self.getRightChildIndex(parentIndex)]
    
    def parent(self, childIndex):
        return self.heap[self.getParentIndex(childIndex)]
    
    def swap(self, indexOne, indexTwo):
        temp = self.heap[indexOne]
        self.heap[indexOne] = self.heap[indexTwo]
        self.heap[indexTwo] = temp

    def add(self, data):
        self.heap.append(data)
        self.size = self.size + 1
        self.siftUp()
        
    def remove(self):   
        self.heap[0] = self.heap[-1]
        self.size = self.size - 1
        self.heapifyDown()
        return self.heap[0]
    
    def siftUp(self):
        # Bubble up the item we just inserted at the bottom of the
        # heap during the add operation
        index = self.size-1
        while(self.hasParent(index) and self.heap[index] < 
              self.parent(index)):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex
        
    
    def heapifyDown(self):  
        # Bubble down the item we just placed at the top of the 
        # heap during the remove operation
        index = 0
        while(self.hasLeftChild(index)):
            smallerChildIndex = self.getLeftChildIndex(index)
            if self.hasRightChildIndex and self.rightChild(index):
                smallerChildIndex = self.getRightChildIndex(index)
            
            if self.heap[index] < self.heap[smallerChildIndex]:
                break
            else:
                self.swap(index, smallerChildIndex)
                
                
    
    
insertItems = [0, 1, 3, 2, -4, 9, 1, 2]
h1 = MinHeap()
for i in insertItems:
    h1.add(i)
    print("Added ", i)
    print("Min is ", h1.peek())
h1.printUnderlyingArray()
for i in range(len(insertItems)):
    print("Removed ", h1.remove())
    print("Min is", h1.peek())
h1.printUnderlyingArray()
