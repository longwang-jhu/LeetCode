# divide and conquer
# get_ancestor: return None if contains neither nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p == None or q == None:
            return None
        return self.get_ancestor(root, p, q)
    
    def get_ancestor(self, root, p, q):
        if root == None or root == p or root == q:
            return root
        
        left = self.get_ancestor(root.left, p, q)
        right = self.get_ancestor(root.right, p, q)
        
        if left != None and right != None: # p and q are seperated
            return root
        if left != None: # p and q are both in left
            return left
        if right != None: # p and q are both in left
            return right
        return None # empty