class Solution:
    def delete_node(self, head, x):
        if head is None or x <= 0:
            return head

        # Case 1: delete head node
        if x == 1:
            head = head.next
            if head:
                head.prev = None
            return head

        current = head
        count = 1

        # Move to the x-th node
        while current and count < x:
            current = current.next
            count += 1

        # If position is out of range
        if current is None:
            return head

        # Adjust pointers
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev

        return head
