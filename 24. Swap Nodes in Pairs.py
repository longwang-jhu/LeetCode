# https://leetcode.com/problems/swap-nodes-in-pairs/

# Given a linked list, swap every two adjacent nodes and return its head. You must
# solve the problem without modifying the values in the list's nodes (i.e., only
# nodes themselves may be changed.)

################################################################################

# SLL swap -> foward traversal
# prev -> (curr -> next) -> ... becomes
# prev -> (next -> curr) -> ...

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        dummy = ListNode()
        dummy.next = head
        
        # prev -> curr
        prev = dummy
        curr = head
        
        while curr and curr.next: # stop at curr = tail or tail.next
            # prev -> (curr -> next) -> ...
            next = curr.next 
            
            # want to do: prev -> (next -> curr) -> ...
            prev.next = next
            curr.next, next.next = next.next, curr

            prev, curr = curr, curr.next # move on
        return dummy.next
