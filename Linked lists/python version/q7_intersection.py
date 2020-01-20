
class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

class Unsorted_ll:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        current = self.head
        if current == None:
            self.head = Node(data)
        else:
            while current.next != None:
                current = current.next
            current.next = Node(data)
    
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

    def attach(self, l2):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = l2.head

def intersects(l1, l2):
    last_node1 = l1.head
    last_node2 = l2.head
    while last_node1.next != None:
        last_node1 = last_node1.next
    while last_node2.next != None:
        last_node2 = last_node2.next
    return id(last_node1) == id(last_node2)



l1 = Unsorted_ll()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(20)
l1.append(20)
l1.display()

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



































