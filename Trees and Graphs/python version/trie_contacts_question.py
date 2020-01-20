
# Create a contacts list. You need to be able to add new contacts
# to it and given a string, figure out how many contacts start with 
# string. Tries are good for this task. For each node, you should 
# store the number of children it has. This is easy to implement but
# it makes the code a lot more efficient and shorter to write.


class Contacts(object):
    class Node(object):
        def __init__(self):
            self.children = [None] * 26
            self.size = 0
            
        def getCharIndex(self, c):
            # Returns the array index that character is located at
            return ord(c) - ord('a')
        
        def getNode(self, c):
            return self.children[self.getCharIndex(c)]
        
        def setNode(self, c):
            self.children[self.getCharIndex(c)] = Node()
        
        def add(self, string):
            self.add2(s, 0)
        
        def add2(self, string, index):
            self.size = self.size + 1
            if index == len(s):
                return
            current = s[index]
            charCode = self.getCharIndex(current)
            child = getNode(current)
            if child == None:
                child = Node()
                setNode(current, child)
            child.add2(s, index + 1)
            
        def findCount(string, index):
            if index == len(string):
                return self.size
            child = getNode(string[index])
            if child == None:
                return 0
            return child.findCount(string, index + 1)
    
    
    def __init__(self):
        
        
    def add(self, name):
        
        
    def findCount(self, prefix)
    
    