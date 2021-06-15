# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Given two integer arrays inorder and postorder where inorder is the inorder
# traversal of a binary tree and postorder is the postorder traversal of the same
# tree, construct and return the binary tree.

################################################################################

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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        n = len(postorder)
        self.inorder = inorder
        self.postorder = postorder
        return self.build(0, n - 1, 0, n - 1)
    
    def build(self, in_start, in_end, post_start, post_end):
        if post_start > post_end: return None
        
        root_val = self.postorder[post_end]
        # get the root_index in inorder
        in_root_idx = self.inorder.index(root_val, in_start, in_end + 1)
        left_len = in_root_idx - in_start
        
        # create node
        root = TreeNode(root_val)
        root.left = self.build(in_start, in_root_idx - 1,
                               post_start, post_start + left_len - 1)
        root.right = self.build(in_root_idx + 1, in_end,
                                post_start + left_len, post_end - 1)
        return root
