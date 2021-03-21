# BFS with deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        depth = 1
        
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.left and not node.right: # no child
                    return depth
            depth += 1        
        return depth