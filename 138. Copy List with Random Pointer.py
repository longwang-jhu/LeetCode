# https://leetcode.com/problems/copy-list-with-random-pointer/

# A linked list of length n is given such that each node contains an additional
# random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n
# brand new nodes, where each new node has its value set to the value of its
# corresponding original node. Both the next and random pointer of the new nodes
# should point to new nodes in the copied list such that the pointers in the
# original list and copied list represent the same list state. None of the
# pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random
# --> Y, then for the corresponding two nodes x and y in the copied list, x.random
# --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each
# node is represented as a pair of [val, random_index] where:

# Your code will only be given the head of the original linked list.

################################################################################

# 1) create 1 -> 1' -> 2 -> 2' -> ...
# 2) assign random ptr
# 3) extra copy and restor original

# other methods: dict, defaultdict

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        
#         # create 1 -> 1' -> 2 -> 2' -> ...
#         curr = head
#         while curr: # stop at curr = tail.next
#             copy = Node(curr.val)
            
#             next = curr.next
#             curr.next = copy
#             copy.next = next
            
#             curr = next
        
#         # assign random ptr
#         curr = head
#         while curr:
#             if curr.random:
#                 curr.next.random = curr.random.next
#             curr = curr.next.next
        
#         # restore
#         curr = head
#         copy_dummy = Node(0) # for copy list
#         copy_curr = copy_dummy
        
#         while curr:
#             # extract copy
#             copy = curr.next
#             copy_curr.next = copy
#             copy_curr = copy_curr.next
        
#             # restore orginal
#             curr.next = curr.next.next
#             curr = curr.next
#         return copy_dummy.next
    
        ### dict ###
        code_copy_map = dict() # key = node, val = copy_node
        
        # copy all node.val
        curr = head
        while curr:
            code_copy_map[curr] = Node(curr.val)
            curr = curr.next
        
        # copy node.next and node.random
        curr = head
        while curr:
            curr_copy = code_copy_map[curr]
            if curr.next: # curr.next can be None
                curr_copy.next = code_copy_map[curr.next]
            if curr.random: # curr.random can be None
                curr_copy.random = code_copy_map[curr.random]
            curr = curr.next
        return code_copy_map[head]
    
        ### defaultdict ###
#         node_copy_map = collections.defaultdict(lambda: Node(0)) 
#         node_copy_map[None] = None # for curr.next = None or curr.random = None
        
#         curr = head
#         while curr:
#             curr_copy = node_copy_map[curr]
#             curr_copy.val = curr.val
#             curr_copy.next = node_copy_map[curr.next] # will create key if not exist
#             curr_copy.random = node_copy_map[curr.random]
#             curr = curr.next      
#         return node_copy_map[head]

