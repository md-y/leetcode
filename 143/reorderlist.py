# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return

        fast_node = head.next.next
        
        if not fast_node:
            return 

        slow_node = head.next
        prev_node = head
        head.next = None

        while fast_node and fast_node.next:
            # Reverse list up to slow pointer
            next_node = slow_node.next
            slow_node.next = prev_node
            prev_node = slow_node
            slow_node = next_node

            fast_node = fast_node.next.next

        # Middle is current node and will be tail
        curr_node = slow_node
        slow_node = slow_node.next
        curr_node.next = None

        even = fast_node is None
        while slow_node or prev_node:
            if even:
                next_node = prev_node.next
                prev_node.next = curr_node
                curr_node = prev_node
                prev_node = next_node
            else:
                next_node = slow_node.next
                slow_node.next = curr_node
                curr_node = slow_node
                slow_node = next_node
            even = not even

