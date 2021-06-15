# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Given the head of a sorted linked list, delete all duplicates such that each
# element appears only once. Return the linked list sorted as well.

################################################################################

# use curr and skip the next node if duplicates

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        curr = head
        while curr.next:
            if curr.val == curr.next.val: # skip the next node
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head
