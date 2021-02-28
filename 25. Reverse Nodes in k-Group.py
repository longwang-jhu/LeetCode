# reverse every sub-ListNode of length k

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # reverse a ListNode
    # def reverse(self, head: ListNode, tail: ListNode):
    #     ptrTailNext = tail.next
    #     ptrHead = head
    #     while ptrTailNext != tail: # 1(head) -> 2 -> 3 -> 4(tail) -> (tailNext)
    #         ptrHeadNext = ptrHead.next # 1(head) -> 2(headNext) -> 3 -> 4(tail) -> (tailNext)
    #         ptrHead.next = ptrTailNext # 2(headNext) -> 3 -> 4(tail) -> (tailNext) <- 1(head)
    #         ptrTailNext = ptrHead # 2(headNext) -> 3 -> 4(tail) -> 1(head) -> (tailNext) 
    #         ptrHead = ptrHeadNext # 2(head) -> 3 -> 4(tail) -> 1(head) -> (tailNext) 
    #     return tail, head
    
    def reverse(self, head: ListNode, tail: ListNode):
        # 0 -> 1(head) -> 2 -> 3(tail) -> tailNext
        dummyHead = ListNode(0)
        dummyHead.next = head
        tailNext = tail.next
        
        prev = dummyHead
        curr = dummyHead.next
        while curr != tailNext:
            temp = curr.next # None(prev) -> 1(curr) -> 2(temp) -> 3 -> None
            curr.next = prev # None(prev) <- 1(curr)   2(temp) -> 3 -> None
            prev = curr
            curr = temp # None <- 1(prev)   2(curr) -> 3 -> None
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        ptrCurr = dummyHead

        while head:
            tail = ptrCurr
            for i in range(k): # move tail for k steps
                tail = tail.next
                if not tail: # reach the end
                    return dummyHead.next
            
            ptrTailNext = tail.next # (curr) -> head -> ... -> tail -> (tailNext)
            
            head, tail = self.reverse(head, tail)
            # reconnect
            ptrCurr.next = head
            tail.next = ptrTailNext
            # move ptrCurr and head
            ptrCurr = tail
            head = ptrCurr.next
        
        return dummyHead.next