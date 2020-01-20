class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add(self, data):
        if data <= self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = Node(data)
                
    def display_in_order(self):
        if self != None:
            if self.left:
                self.left.display_in_order()
            print(self.data)
            if self.right:
                self.right.display_in_order()
    
    def display_pre_order(self):
        if self != None:
            print(self.data)
            if self.left:
                self.left.display_pre_order()
            if self.right:
                self.right.display_pre_order()
    
    def display_post_order(self):
        if self != None:
            if self.left:
                self.left.display_post_order()
            if self.right:
                self.right.display_post_order()
            print(self.data)

class Bst:
            
    def __init__(self):
        self.root = None
    
    def add(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.root.add(data)
    
    def display_in_order(self):
        self.root.display_in_order()
        
    def display_pre_order(self):
        self.root.display_pre_order()
    
    def display_post_order(self):
        self.root.display_post_order()
    

b1 = Bst()
b1.add(50)
b1.add(30)
b1.add(40)
b1.add(10)
b1.add(20)
b1.add(35)
b1.add(70)
b1.add(90)
b1.add(60)
b1.display_in_order()





































            
        