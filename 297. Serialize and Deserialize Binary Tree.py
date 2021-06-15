# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work. You
# just need to ensure that a binary tree can be serialized to a string and this
# string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a
# binary tree. You do not necessarily need to follow this format, so please be
# creative and come up with different approaches yourself.

################################################################################

# bfs

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None: return ''
        
        queue = deque([root])
        bfs_order = []
        while queue:
            node = queue.popleft()
            if node:
                bfs_order.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                bfs_order.append("#")       
        return ' '.join(bfs_order)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        
        # get all the nodes
        bfs_order = []
        for val in data.split():
            if val == '#':
                bfs_order.append(None)
            else:
                bfs_order.append(TreeNode(int(val)))
        
        # add connections
        i = 1
        queue = deque([bfs_order[0]])
        while queue:
            # add child
            node = queue.popleft()
            node.left = bfs_order[i]
            node.right = bfs_order[i + 1]
            i += 2 # move ptrs
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return bfs_order[0]       

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
