# https://leetcode.com/problems/sort-list/

# Given the head of a linked list, return the list after sorting it in
# ascending order.

# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory
# (i.e. constant space)?

###############################################################################

# merge sort
# find mid node using slow and fast ptrs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # divide and conquer
        mid = self.find_mid_node(head)
        right = self.sortList(mid.next)
        
        mid.next = None
        left = self.sortList(head)
        
        # merge
        return self.merge(left, right)
    
    def find_mid_node(self, head):
        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def merge(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        
        return dummy.next