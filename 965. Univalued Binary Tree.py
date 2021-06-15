# https://leetcode.com/problems/univalued-binary-tree/

# A binary tree is univalued if every node in the tree has the same value.

# Return true if and only if the given tree is univalued.

################################################################################

# divide and conquer

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root: return True
        
        if root.left and root.val != root.left.val:
            return False
        if root.right and root.val != root.right.val:
            return False
        
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
