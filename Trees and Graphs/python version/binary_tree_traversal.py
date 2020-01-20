

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
            
            
            
root = Node(50)
root.add(30)
root.add(40)
root.add(10)
root.add(20)
root.add(35)
root.add(70)
root.add(90)
root.add(60)
root.display_in_order()
root.display_post_order()
root.display_pre_order()

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            