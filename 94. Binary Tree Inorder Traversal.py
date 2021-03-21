# stack: append(curr), go left, if no more left, pop, print and go right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        curr = root
        
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else: # go to right child
                node = stack.pop()
                ans.append(node.val)
                curr = node.right
        return ans