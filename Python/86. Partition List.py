# https://leetcode.com/problems/partition-list/

# Given the head of a linked list and a value x, partition it such that all
# nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the
# two partitions.

###############################################################################

# use dummy_left and dummy_right and merge afterwards

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy_left = ListNode()
        dummy_right = ListNode()
        
        left, right, curr = dummy_left, dummy_right, head
        
        while curr:
            if curr.val < x:
                left.next = curr
                left = left.next
            else:
                right.next = curr
                right = right.next
            curr = curr.next
        
        # merge left and right
        left.next = dummy_right.next
        right.next = None
        return dummy_left.next