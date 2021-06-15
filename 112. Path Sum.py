# https://leetcode.com/problems/path-sum/

# Given the root of a binary tree and an integer targetSum, return true if the
# tree has a root-to-leaf path such that adding up all the values along the path
# equals targetSum.

# A leaf is a node with no children.

################################################################################

# divide and conquer

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        
        has_left = self.hasPathSum(root.left, targetSum - root.val)
        has_right = self.hasPathSum(root.right, targetSum - root.val)
        
        return has_left or has_right
