# https://leetcode.com/problems/binary-tree-paths/

# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

################################################################################

# dfs(node)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        
        self.ans = []
        self.holder = [str(root.val)]
        self.dfs(root)
        return self.ans
    
    def dfs(self, node):
        if not node.left and not node.right:
            self.ans.append("->".join(self.holder))
            return
        
        if node.left:
            self.holder.append(str(node.left.val))
            self.dfs(node.left)
            self.holder.pop()
        if node.right:
            self.holder.append(str(node.right.val))
            self.dfs(node.right)
            self.holder.pop()
