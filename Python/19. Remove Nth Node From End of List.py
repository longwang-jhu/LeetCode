# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Given the head of a linked list, remove the nth node from the end of the list
# and return its head.

# Follow up: Could you do this in one pass?

###############################################################################

# linked list -> nth node from end -> slow and fast ptrs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, dummy
        
        # move fast n time
        for _ in range(n):
            fast = fast.next
        
        # move fast and slow together
        while fast.next: # stop at fast = tail, slow.next = desired node
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next # skip the desired node
        return dummy.next