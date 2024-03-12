from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, head)
        curr = head.next
        prev_sums = { 0: head }
        curr_sum = 0
        
        while curr:
            curr_sum += curr.val
            prev_sums[curr_sum] = curr
            curr = curr.next

        curr_sum = 0
        curr = head
        while curr:
            curr_sum += curr.val
            curr.next = prev_sums[curr_sum].next
            curr = curr.next
        return head.next




head = ListNode()
prev_node = None
for i in [100, 1, 2, 3, 4, -10, 69]:
    if prev_node == None:
        head.val = i
        prev_node = head
    else:
        node = ListNode()
        node.val = i
        prev_node.next = node
        prev_node = node

sol = Solution()
res = sol.removeZeroSumSublists(head)
while res != None:
    print(res.val)
    res = res.next

