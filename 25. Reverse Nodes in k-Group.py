# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Given a linked list, reverse the nodes of a linked list k at a time and return
# its modified list.

# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes, in the
# end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be
# changed.

################################################################################

# reverse every sub-ListNode of length k
# curr = dummy, move k steps to make curr = tail
# prev -> (head -> ... -> tail) -> next
# prev -> (tail -> ... -> head) -> next
# separate func to reverse (head, tail)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head, tail):
        prev, curr = None, head
        while prev != tail:
            next = curr.next # (prev -> curr) -> next
            curr.next = prev # (prev <- curr)    next
            
            prev, curr = curr, next # move on
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        prev = curr = dummy

        while curr.next:
            for i in range(k): # move curr k steps to make curr = tail
                curr = curr.next
                if not curr: # curr = None, not tail
                    return dummy.next
            
            # prev -> (head -> ... -> tail) -> next
            head = prev.next
            tail = curr
            next = curr.next
            
            tail, head = self.reverse(head, tail)
            
            # reconnect: prev -> (tail -> ... -> head) -> next
            prev.next = tail
            head.next = next

            # move prev and curr
            prev = curr = head
        return dummy.next
