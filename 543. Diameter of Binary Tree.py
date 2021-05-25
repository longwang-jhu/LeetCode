# https://leetcode.com/problems/diameter-of-binary-tree/

# Given the root of a binary tree, return the length of the diameter of the
# tree.

# The diameter of a binary tree is the length of the longest path between any
# two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges
# between them.

###############################################################################

# longest path must be leaf-to-leaf
# -> sum of longest left and right branches
# -> divide and conquer

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        self.longest_path(root)
        return self.ans
    
    def longest_path(self, node):
        if not node: return 0
        
        left_longest = self.longest_path(node.left)
        right_longest = self.longest_path(node.right)      
        self.ans = max(self.ans, left_longest + right_longest)
        
        return max(left_longest, right_longest) + 1