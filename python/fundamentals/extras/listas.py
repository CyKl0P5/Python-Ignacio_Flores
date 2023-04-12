class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SNode(val)


class SNode:
    def __init__(self):
        self.head = None

    def add_to_front(self,val):
        new_node = SList(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self


