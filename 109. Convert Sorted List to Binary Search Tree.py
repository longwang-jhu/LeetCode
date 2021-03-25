# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Given the head of a singly linked list where elements are sorted in ascending
# order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.

###############################################################################

# divide and conquer
# find middle node first, break the list before the mid node
# tree_node.left = self.sortedListToBST(head)
# tree_node.right = self.sortedListToBST(node.next)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        # find the mid node and make it root
        node = self.find_mid_node(head)
        tree_node = TreeNode(node.val)       
        tree_node.left = self.sortedListToBST(head)
        tree_node.right = self.sortedListToBST(node.next)
        
        return tree_node

    def find_mid_node(self, head):
        prev = None
        slow, fast = head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # break the list at .. -> prev -x-> slow -> ...
        if prev:
            prev.next = None
        
        return slow