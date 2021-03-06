# find length, then the new head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return
        
        # find length first
        length = 1
        curr = head       
        while curr.next != None:
            curr = curr.next
            length += 1
        
        # find new head
        k = k % length
        curr.next = head # cycle the list
        curr = curr.next
        for _ in range(length - k - 1): # stop right before the head
            curr = curr.next
        
        head = curr.next
        curr.next = None
        return head