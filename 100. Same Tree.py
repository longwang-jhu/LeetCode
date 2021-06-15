# https://leetcode.com/problems/same-tree/

# Given the roots of two binary trees p and q, write a function to check if they
# are the same or not.

# Two binary trees are considered the same if they are structurally identical, and
# the nodes have the same value.

################################################################################

# divide and conquer

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        
        if not q or not p:
            return False
        
        if p.val != q.val:
            return False
        
        if not self.isSameTree(p.left, q.left):
            return False
        
        if not self.isSameTree(p.right, q.right):
            return False
        
        return True
