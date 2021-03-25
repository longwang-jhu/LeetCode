# https://leetcode.com/problems/binary-tree-paths/

# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

###############################################################################

# dfs(root, path, ans)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        ans = []
        self.dfs(root, '', ans)
        return ans
    
    def dfs(self, root, path, ans):
        if not root.left and not root.right:
            ans.append(path + str(root.val))
        
        if root.left:
            self.dfs(root.left, path + str(root.val) + '->', ans)
        if root.right:
            self.dfs(root.right, path + str(root.val) + '->', ans)