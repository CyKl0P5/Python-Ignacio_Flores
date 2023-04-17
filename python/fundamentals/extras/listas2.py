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
            return
        runner = self.root
        while runner.next != None:
            runner = runner.next
        new_node = Node(data)
        runner.next = new_node
        new_node.prev = runner
        return self

    def ide(self, n, data):
        if self.root == None:
            print("L/V")
        else:
            runner = self.root
            while runner != None:
                if runner.value == n:
                    break
                runner = runner.next
            if runner == None:
                print("N/F")
            else:
                new_node = Node(data)
                new_node.prev = runner
                new_node.next = runner.next
                if runner.next != None:
                    runner.next.prev = new_node
                runner.next = new_node

    def delI(self):
        if self.root == None:
            print("L/V")
            return
        if self.root.next == None:
            self.root = None
        self.root = self.root.next
        self.root.prev = None
        return self

    def delB(self):
        if self.root == None:
            print("L/V")
            return
        if self.root.next == None:
            self.root = None
            return
        runner = self.root
        while runner.next != None:
            runner = runner.next
        runner.prev.next = None
        return self

    def debValued(self, val):
        if self.root == None:
            print("L/V")
        elif self.root.next == None:
            if self.root.value == val:
                self.root = None
            else:
                print("N/F")
        elif self.root.value == val:
            self.delI()
        runner = self.root
        while runner.next != None:
            if runner.value == val:
                break
            runner = runner.next


