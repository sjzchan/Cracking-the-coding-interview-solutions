
class animalShelter:
    class Queue:
        class Node:
            def __init__(self, data=0):
                self.data = data
                self.prev = None
        
        def __init__(self):
            self.tail = None
            self.head = None
            
        def enqueue(self, data):
            if self.head == None:
                self.head = self.Node(data)
                self.tail = self.head
            else:
                newNode = self.Node(data)
                self.tail.prev = newNode
                self.tail = newNode
        
        def dequeue(self):
            self.head = self.head.prev
            
        def display(self):
            elems = []
            current = self.head
            while current != None:
                elems.append(current.data)
                current = current.prev
            print(elems)
            
    def __init__(self):
        self.queueDog = self.Queue()
        self.queueCat = self.Queue()
        self.time = 0
        
    def incrementTime(self):
        self.time = self.time + 1
        
    def enqueueDog(self):
        self.queueDog.enqueue(self.time)
        self.incrementTime()
    
    def enqueueCat(self):
        self.queueCat.enqueue(self.time)
        self.incrementTime()
    
    def dequeueDog(self):
        self.queueDog.dequeue()

    def dequeueCat(self):
        self.queueCat.dequeue()

    def dequeueAny(self):
        if self.queueDog.head != None:
            if self.queueCat.head != None:
                if self.queueDog.head.data < self.queueCat.head.data:
                    self.dequeueDog()
                else:
                    self.dequeueCat()
            else:
                self.dequeueDog()
        else:
            if self.queueCat.head != None:
                self.dequeueCat()
            
    def display(self):
        self.queueDog.display()
        self.queueCat.display()
            
a1 = animalShelter()
a1.enqueueCat()
a1.enqueueDog()
a1.enqueueCat()
a1.enqueueCat()
a1.enqueueDog()
a1.enqueueCat()
a1.enqueueDog()
a1.enqueueDog()
a1.enqueueCat()
a1.display()
a1.dequeueAny()
a1.display()



























