# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''
        This butchers the list in-place
        '''

        if head == None or head.next == None:
            return True

        fast_node = head.next.next

        # Only 2
        if fast_node == None:
            return head.val == head.next.val

        slow_node = head.next
        prev_node = head

        while fast_node and fast_node.next:
            # Reverse slow node
            next_node = slow_node.next
            slow_node.next = prev_node
            prev_node = slow_node
            slow_node = next_node

            fast_node = fast_node.next.next

        # Odd (can skip middle number)
        if fast_node != None:
            slow_node = slow_node.next

        while prev_node and slow_node:
            if prev_node.val != slow_node.val:
                return False
            slow_node = slow_node.next
            prev_node = prev_node.next
        return True

arr = list(range(1, 10)) + list(range(9, 0, -1)) 
print(arr)
head = curr_node = ListNode(arr[0], None)
for i in arr[1:]:
    curr_node.next = ListNode(i, None)
    curr_node = curr_node.next

sol = Solution()
res = sol.isPalindrome(head)
print(res)
