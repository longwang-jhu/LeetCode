# https://leetcode.com/problems/subtree-of-another-tree/

# Given the roots of two binary trees root and subRoot, return true if there is a
# subtree of root with the same structure and node values of subRoot and false
# otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and
# all of this node's descendants. The tree tree could also be considered as a
# subtree of itself.

################################################################################

# get preorder, use l_None and r_None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.has_subtree(s, t)
    
        s_preorder = self.preorder(s, True)
        t_preorder = self.preorder(t, True)       
        return s_preorder.find(t_preorder) >= 0
    
    def preorder(self, node, is_left):
        if not node:
            if is_left:
                return 'l_None'
            else:
                return "r_None"
        
        return "#" + str(node.val) + " " \
                   + self.preorder(node.left, True) + " " \
                   + self.preorder(node.right, False)
    
# treat every node in s as root, compare with t
    def has_subtree(self, s, t):
        if s is None:
            return False
        
        return self.is_same(s,t) \
               or self.has_subtree(s.left, t) \
               or self.has_subtree(s.right, t)
    
    def is_same(self, s, t):
        if s is None and t is None: return True # both are None
        if s is None or t is None: return False # only one is None
        
        return s.val == t.val \
               and self.is_same(s.left, t.left) \
               and self.is_same(s.right, t.right)
