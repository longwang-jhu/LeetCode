# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Given the root of a binary search tree, and an integer k, return the kth
# (1-indexed) smallest element in the tree.

###############################################################################

# inorder = sorted ascending list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # return self.inorder_stack(root, k)
        
        inorder_list = self.inorder(root)
        return inorder_list[k - 1]
        
    def inorder(self, root):
        if not root:
            return []
        
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
        
    
    def inorder_stack(self, root, k):
        stack = []
        
        while True:
            # travel all the way to the left
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right # go to right        