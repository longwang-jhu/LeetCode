# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Given the head of a sorted linked list, delete all nodes that have duplicate
# numbers, leaving only distinct numbers from the original list. Return the
# linked list sorted as well.

###############################################################################

# use curr and record the duplicated value

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        
        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val: # duplicate
                dup_val = curr.next.val
                while curr.next and curr.next.val == dup_val:
                    curr.next = curr.next.next
            else: # no duplicate
                curr = curr.next
                
        return dummy.next