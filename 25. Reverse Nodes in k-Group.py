# reverse every sub-ListNode of length k

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, tail):
        prev, curr = None, head
        while prev != tail:
            next = curr.next # prev -> curr -> next
            curr.next = prev
            prev, curr = curr, next # move on
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy_head = ListNode(None)
        dummy_head.next = head
        prev = dummy_head

        while prev.next:
            tail = prev
            for i in range(k): # move tail for k steps
                tail = tail.next
                if not tail: # reach end: tail == None
                    return dummy_head.next
            
            next = tail.next # prev -> head -> ... -> tail -> next
            print("head, tail value", head.val, tail.val)
            head, tail = self.reverse(head, tail)
            
            # reconnect prev -> head -> ... -> tail -> next
            prev.next = head
            tail.next = next

            # move prev and head
            prev, head = tail, next
        
        return dummy_head.next