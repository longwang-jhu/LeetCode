# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Given the root of a binary tree, return the preorder traversal of its nodes'
# values.

################################################################################

# stack: append(curr), print, go left, if no more left, pop and go right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                ans.append(curr.val)
                curr = curr.left
            else: # go to right child
                node = stack.pop()
                curr = node.right
        return ans
    
#         if not root:
#             return []
               
#         ans = []
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             ans.append(node.val)
            
#             # put in right child first
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
        
#         return ans
