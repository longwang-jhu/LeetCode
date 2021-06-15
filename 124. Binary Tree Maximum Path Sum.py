# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
# in the sequence has an edge connecting them. A node can only appear in the
# sequence at most once. Note that the path does not need to pass through the
# root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any path.

################################################################################

# divide and conquer
# single_path: start from curr node, can be None
# max_path: cannot be None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return self.helper(root)[1]
    
    # return (single_path, max_path)
    def helper(self, root):
        if root == None:
             return (0, float("-inf"))
        
        l_single_path, l_max_path = self.helper(root.left)
        r_single_path, r_max_path = self.helper(root.right)
        
        single_path = max(l_single_path, r_single_path) + root.val # choose left or right
        single_path = max(single_path, 0) # might be better to just be None
        
        max_path = max(l_max_path, r_max_path)
        max_path = max(max_path, l_single_path + r_single_path + root.val) # passing curr node
        
        return (single_path, max_path)
