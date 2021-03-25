# https://leetcode.com/problems/cousins-in-binary-tree/

# In a binary tree, the root node is at depth 0, and children of each depth k
# node are at depth k+1.

# Two nodes of a binary tree are cousins if they have the same depth, but have
# different parents.

# We are given the root of a binary tree with unique values, and the values x
# and y of two different nodes in the tree.

# Return true if and only if the nodes corresponding to the values x and y are
# cousins.

###############################################################################

# BFS with Dict[node_val] = parent_val

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = deque([root])
        
        while queue:
            parent_dict = {}
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    parent_dict[node.left.val] = node.val
                if node.right:
                    queue.append(node.right)
                    parent_dict[node.right.val] = node.val
            
            if x in parent_dict and y in parent_dict and parent_dict[x] != parent_dict[y]:
                return True
        return False