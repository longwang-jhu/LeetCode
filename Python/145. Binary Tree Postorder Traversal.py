# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Given the root of a binary tree, return the postorder traversal of its nodes'
# values.

###############################################################################

# stack: perorder but go right first, then reverse answer

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        curr = root
        
        while curr or stack:
            if curr:
                stack.append(curr)
                ans.append(curr.val)
                curr = curr.right
            else: # go to right child
                node = stack.pop()
                curr = node.left
        return ans[::-1]