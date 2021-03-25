# https://leetcode.com/problems/balanced-binary-tree/

# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in
# height by no more than 1.

###############################################################################

# divide and conquer
# check: 1) root.left is balanced; 2) root.right is balanced; 3) | len(root.left) - len(root.right) | <= 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.max_depth(root) != -1
        
    def max_depth(self, root):
        if root == None:
            return 0
        
        l_depth = self.max_depth(root.left)
        r_depth = self.max_depth(root.right)
        
        # return -1 if not balanced
        if l_depth == -1 or r_depth == -1 or abs(l_depth - r_depth) > 1:
            return -1
        else:
            return max(l_depth, r_depth) + 1