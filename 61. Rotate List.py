# https://leetcode.com/problems/rotate-list/

# Given the head of a linked list, rotate the list to the right by k places.

################################################################################

# SLL -> forward traversal -> find length -> find new head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head
        
        # find length first
        length = 1
        curr = head       
        while curr.next != None: # stop at curr = tail
            curr = curr.next
            length += 1
        curr.next = head # cycle the list
        
        # find new_head
        k = k % length
        curr = head
        for _ in range(length - k - 1): # stop at curr -> new_head -> ...
            curr = curr.next
        
        head = curr.next
        curr.next = None
        return head
