class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def reverse_ll(self, head):
        if head is None or head.next is None:
            return head

        current = head
        new_head = None

        while current is not None:
            # Swap prev and next
            temp = current.prev
            current.prev = current.next
            current.next = temp

            # Update new head
            new_head = current

            # Move to next node (which is previous due to swap)
            current = current.prev

        return new_head
