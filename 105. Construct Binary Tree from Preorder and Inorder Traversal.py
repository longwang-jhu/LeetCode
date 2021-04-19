# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same
# tree, construct and return the binary tree.

###############################################################################

# divide and conquer
# find index of root in inorder
# preorder:  [root, ...root_left..., ...root_right...]
# inorder:   [...root_left..., root, ...root_right...]
# postorder: [...root_left..., ...root_right..., root]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)
        self.preorder = preorder
        self.inorder = inorder
        return self.build(0, n - 1, 0, n - 1)
    
    def build(self, pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end: return None
        
        root_val = self.preorder[pre_start]
        # get the root_index in inorder
        in_root_idx = self.inorder.index(root_val, in_start, in_end + 1)
        left_len = in_root_idx - in_start
        
        # create node
        root = TreeNode(root_val)
        root.left = self.build(pre_start + 1, pre_start + left_len,
                              in_start, in_root_idx - 1)
        root.right = self.build(pre_start + left_len + 1, pre_end,
                              in_root_idx + 1, in_end)
        return root