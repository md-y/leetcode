class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr_node = list1
        for _ in range(a - 1):
            curr_node = curr_node.next
        a_node = curr_node

        for _ in range(b - a + 2):
            curr_node = curr_node.next
        b_node = curr_node

        list2_tail = a_node.next = list2

        while list2_tail.next:
            list2_tail = list2_tail.next
        list2_tail.next = b_node

        return list1
