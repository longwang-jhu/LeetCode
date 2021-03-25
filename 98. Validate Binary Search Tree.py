# https://leetcode.com/problems/validate-binary-search-tree/

# Given the root of a binary tree, determine if it is a valid binary search
# tree (BST).

# A valid BST is defined as follows:

###############################################################################

# divide and conquer, record (is_valid, min_val, max_val)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.valid_BST(root)[0]
    
    def valid_BST(self, root):
        if not root:
            return (True, float("-inf"), float("inf"))
        
        left_valid, left_min, left_max = self.valid_BST(root.left)
        right_valid, right_min, right_max = self.valid_BST(root.right)
        
        if root.left and root.right:
            if not left_valid or not right_valid or not (left_max < root.val < right_min):
                return (False, None, None)
            else:
                return (True, left_min, right_max)

        if root.left and not root.right: # no right child
            if not left_valid or not (left_max < root.val):
                return (False, None, None)
            else:
                return (True, left_min, root.val)

        if not root.left and root.right: # no left child
            if not right_valid or not (root.val < right_min):
                return (False, None, None)
            else:
                return (True, root.val, right_max)

        if not root.right and not root.left: # no left and right children
            return (True, root.val, root.val)           