class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def constructDLL(self, arr):
        if not arr:
            return None

        head = None
        tail = None

        for val in arr:
            new_node = Node(val)

            if head is None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                new_node.prev = tail
                tail = new_node

        return head
