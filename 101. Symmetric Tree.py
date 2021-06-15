# https://leetcode.com/problems/symmetric-tree/

# Given the root of a binary tree, check whether it is a mirror of itself (i.e.,
# symmetric around its center).

################################################################################

# divide and conquer -> is_mirror(node1, node2)
# time: O(n); space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_mirror(root, root)
    
    def is_mirror(self, node1, node2):
        if not node1 and not node2: return True
        if not node1 or not node2: return False
        if node1.val != node2.val: return False
        
        return self.is_mirror(node1.right, node2.left) \
               and self.is_mirror(node1.left, node2.right)
