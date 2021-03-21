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