# iteratively: prev -> curr -> next => prev <- curr -x- next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr: # stop when curr == tail.next == None
            next = curr.next # prev -> curr -> next
            curr.next = prev # prev <- curr -x- next
            prev, curr = curr, next # move on
        return prev