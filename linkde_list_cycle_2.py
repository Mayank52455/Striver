class Solution(object):
    def detectCycle(self, head):
        if not head or not head.next:
            return None

        slow = head
        fast = head

        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Step 2: Find cycle start
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        # No cycle
        return None
