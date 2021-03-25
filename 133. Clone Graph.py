# https://leetcode.com/problems/clone-graph/

# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a val (int) and a list (List[Node]) of its
# neighbors.

###############################################################################

# bfs (deque)
# use node_copy_map{key: value} with key = node and val = node.copy

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        node_copy_map = {} # key = node, val = node_copy
        node_copy_map[node] = Node(node.val)
        deque = collections.deque([node])
        
        while deque:
            curr = deque.popleft()
            for neigh in curr.neighbors: # loop over all neighbors
                if neigh not in node_copy_map: # new node, copy node.val
                    node_copy_map[neigh] = Node(neigh.val)
                    deque.append(neigh)
                node_copy_map[curr].neighbors.append(node_copy_map[neigh]) # copy node.neighbors
        
        return node_copy_map[node] # return copy of fisrt node