# https://leetcode.com/problems/clone-graph/

# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a val (int) and a list (List[Node]) of its
# neighbors.

###############################################################################

# bfs -> use copy_dict: key = node, val = node_copy

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        copy_dict = dict() # key = node, val = node_copy
        copy_dict[node] = Node(node.val)
        queue = deque([node])
        
        while queue:
            curr = queue.popleft()
            for neigh in curr.neighbors: # loop over all neighbors
                if neigh not in copy_dict: # copy neighbors
                    copy_dict[neigh] = Node(neigh.val)
                    queue.append(neigh) # only append unvisited neighbours
                copy_dict[curr].neighbors.append(copy_dict[neigh]) # copy connection
        
        return copy_dict[node] # return copy of fisrt node