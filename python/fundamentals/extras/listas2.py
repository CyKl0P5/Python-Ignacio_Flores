class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Elist:
    def __init__(self):
        self.root = None

    def ilv(self, data): 
        if self.root == None:
            new_node = Node(data)
            self.root = new_node
        else: 
            print
        return self


    def atf(self, data):
        if self.root == None:
            self.ilv(data)
            return
        else:
            new_node = Node(data)
            new_node.next = self.root
            self.root.prev = new_node
            self.root = new_node
        return self

    def atb(self, data):
        if self.root == None:
            new_node = Node(data)
            self.root = new_node
