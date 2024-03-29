class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DList:
    def __init__(self):
        self.root = None

    def ilv(self, data):  
        if self.root == None:
            new_node = Node(data)
            self.root = new_node
        else:  
            print("La lista no esta vacia")
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
        if runner.next != None:
            runner.prev.next = runner.next
            runner.next.prev = runner.prev
        else:
            if runner.value == val:
                self.delB()
            else:
                print("N/F")
        print(runner.value, "uwu")
        return self

    def print_info(self):
        if self.root == None:
            print("L/V")
            return
        else:
            runner = self.root
            while runner != None:
                print(runner.value, " ")
                runner = runner.next
        return self

    def LCircular(self):
        runner = self.root
        while runner.next != None:
            runner = runner.next
        if runner.next == None:
            print("No es circular")
        else:
            print("Es circular")
        return self

    def mitad(self):
        runner = self.root
        count = 0
        while runner != None:
            count += 1
            runner = runner.next
        runner_two = self.root
        count = count / 2
        b = 0
        while b < count:
            print(runner_two.value)
            runner_two = runner_two.next
            b += 1
        return self


test = DList()
test.ilv(4)
test.atb(8).atf(1).atf(4).atb(2).atb(5).atf(3).atb(6)
test.print_info()
print("--------------------------------------------------")
test.delI()
test.print_info()
print("--------------------------------------------------")
test.delB()
test.print_info()
print("--------------------------------------------------")
test.debValued(8)
test.print_info()
print("--------------------------------------------------")
test.ide(1, 78)
test.print_info()
print("--------------------------------------------------")
test.countE()
print("--------------------------------------------------")
test.mitad()