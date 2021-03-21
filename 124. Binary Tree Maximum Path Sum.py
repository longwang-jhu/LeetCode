# divide and conquer
# single_path: for passing the root node, can be None
# max_path: cannot be None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return self.helper(root)[1]
    
    # return (single_path, max_path)
    def helper(self, root):
        if root == None:
             return (0, -2**31)
        
        l_single_path, l_max_path = self.helper(root.left)
        r_single_path, r_max_path = self.helper(root.right)
        
        single_path = max(l_single_path, r_single_path) + root.val
        single_path = max(single_path, 0) # might be better to just be None
        
        max_path = max(l_max_path, r_max_path)
        max_path = max(max_path, l_single_path + r_single_path + root.val) # connecting root
        
        return (single_path, max_path)