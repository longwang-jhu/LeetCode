# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Given the head of a linked list, remove the nth node from the end of the list
# and return its head.

# Follow up: Could you do this in one pass?

###############################################################################

# use slow and fast

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # one pass
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, dummy
        
        # move fast n time
        for _ in range(n):
            fast = fast.next
        
        # move fast and slow together
        while fast.next: # stop at fast = tail
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next # skip the desire node
        return dummy.next