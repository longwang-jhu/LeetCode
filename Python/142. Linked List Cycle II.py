# https://leetcode.com/problems/linked-list-cycle-ii/

# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can
# be reached again by continuously following the next pointer. Internally, pos
# is used to denote the index of the node that tail's next pointer is connected
# to. Note that pos is not passed as a parameter.

# Notice that you should not modify the linked list.

###############################################################################

# use slow and fast
# if meet, move slow to head and stop when meet again

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        
        is_cycle = False
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                is_cycle = True
                break
        
        if not is_cycle:
            return None
        else:
            # move slow to head
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow