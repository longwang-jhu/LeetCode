# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Given the root of a binary tree, return the level order traversal of its nodes'
# values. (i.e., from left to right, level by level).

################################################################################

# bfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None: return []
        
        ans = []
        queue = deque([root])
                
        while queue:
            curr_level = []
            curr_level_size = len(queue)
            for _ in range(curr_level_size):
                # append node to curr_level
                node = queue.popleft()
                curr_level.append(node.val)
                # append child to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(curr_level)
        return ans
