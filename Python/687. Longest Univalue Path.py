# https://leetcode.com/problems/longest-univalue-path/

# Given the root of a binary tree, return the length of the longest path, where
# each node in the path has the same value. This path may or may not pass
# through the root.

# The length of the path between two nodes is represented by the number of
# edges between them.

###############################################################################

# divide and conquer
# get straight_len and max_len from root.left and root.right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.straight_len(root)[1]
    
    def straight_len(self, root):
        if not root:
            return 0, 0
        
        left_straight_len, left_max_len = self.straight_len(root.left)
        right_straight_len, right_max_len = self.straight_len(root.right)
        
        if root.left and root.val == root.left.val:
            left_straight_len = left_straight_len + 1
        else:
            left_straight_len = 0
            
        if root.right and root.val == root.right.val:
            right_straight_len = right_straight_len + 1
        else:
            right_straight_len = 0

        return max(left_straight_len, right_straight_len), max(left_max_len, right_max_len, left_straight_len + right_straight_len)