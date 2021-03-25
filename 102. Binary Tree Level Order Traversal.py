# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).

###############################################################################

# use deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        queue = deque([root])
        ans = []
        
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                # append current node to level
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            ans.append(level)
        return ans