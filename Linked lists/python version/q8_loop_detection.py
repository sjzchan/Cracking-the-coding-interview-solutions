
class Unsorted_ll:
    class Node:
        def __init__(self, data=0):
            self.data = data
            self.next = None
        
    def __init__(self):
        self.head = None
    
    def append(self, data):
        current = self.head
        if current == None:
            self.head = self.Node(data)
        else:
            while current.next != None:
                current = current.next
            current.next = self.Node(data)
    
    def display(self):
        elems = []
        current = self.head
        while current != None:
            elems.append(current.data)
            current = current.next
        print(elems)

    def length(self):
        count = 0
        current = self.head
        while current != None:
            count = count + 1
            current = current.next
        return count

    def createLoop(self):
        current = self.head
        loopNode = current.next.next
        while current.next != None:
            current = current.next
        current.next = loopNode

    def loopPoint(self):
        current = self.head
        addresses = set()
        while current.next != None:
            if id(current) in addresses:
                return current.data
            else:
                addresses.add(id(current))
                current = current.next
        return None
        
l1 = Unsorted_ll()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
l1.append(50)
l1.append(60)
l1.createLoop()
l1.loopPoint()

l2 = Unsorted_ll()
l2.append(10)
l2.append(20)
l2.append(20)
l2.append(20)
l2.display()

l3 = Unsorted_ll()
l3.append(200)
l1.attach(l3)
l2.attach(l3)
l1.display()
l2.display()

intersects(l1, l2)




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

