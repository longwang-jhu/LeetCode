# https://leetcode.com/problems/swap-nodes-in-pairs/

# Given a linked list, swap every two adjacent nodes and return its head.

###############################################################################

# use ptrCurr, ptrSwap, ptrSwap1, ptrSwap2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        ptrCurr = dummyHead # current point
        
        dummyHead.next = head
        ptrSwap = head # pointer for swapping
        
        while ptrSwap and ptrSwap.next:
            ptrSwap1 = ptrSwap
            ptrSwap2 = ptrSwap.next
            
            ptrCurr.next = ptrSwap2 # c-> 2 -> 3
            ptrSwap1.next = ptrSwap2.next # 1 -> 3
            ptrSwap2.next = ptrSwap1 # c-> 2-> 1 -> 3
            
            ptrCurr = ptrSwap1 # c -> 3
            ptrSwap = ptrSwap1.next
        
        return dummyHead.next