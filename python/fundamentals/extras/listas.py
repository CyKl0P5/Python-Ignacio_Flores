class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self,val):
        new_node = SList(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def atb(self, val):
        if self.head == None:
            self.add_to_front
        new_node = SNode(val)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node

    def print_values(self):
        runner = self.head
        print(runner.value)
        runner = runner.next

class SNode:
    def __init__(self, val):
        self.value = val
        self.next = None





