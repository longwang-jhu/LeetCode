# https://leetcode.com/problems/validate-binary-search-tree/

# Given the root of a binary tree, determine if it is a valid binary search tree
# (BST).

# A valid BST is defined as follows:

################################################################################

# divide and conquer
# need (is_valid, min_val, max_val) of both sides

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        
        return self.valid_BST(root)[0]
    
    def valid_BST(self, root):
        if not root:
            return True, None, None
        
        l_is_valid, l_min, l_max = self.valid_BST(root.left)
        r_is_valid, r_min, r_max = self.valid_BST(root.right)
        
        if not root.right and not root.left: # no left and right children
            return True, root.val, root.val
        
        if root.left and not root.right: # no right child
            if not l_is_valid or not l_max < root.val:
                return False, None, None
            else:
                return True, l_min, root.val
        
        if not root.left and root.right: # no left child
            if not r_is_valid or not root.val < r_min:
                return False, None, None
            else:
                return True, root.val, r_max
            
        if root.left and root.right:
            if not l_is_valid or not r_is_valid or not l_max < root.val < r_min:
                return False, None, None
            else:
                return True, l_min, r_max
