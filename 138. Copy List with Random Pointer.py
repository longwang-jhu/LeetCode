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
        if not head:
            return None
        
        # create 1 -> 1' -> 2 -> 2' -> ...
        curr = head
        while curr: # stop at curr = tail.next
            copy = Node(curr.val)
            
            next = curr.next
            curr.next = copy
            copy.next = next
            
            curr = next
        
        # assign random ptr
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # restore
        curr = head
        copy_dummy = Node(0) # for copy list
        copy_curr = copy_dummy
        
        while curr:
            # extract copy
            copy = curr.next
            copy_curr.next = copy
            copy_curr = copy_curr.next
        
            # restore orginal
            curr.next = curr.next.next
            curr = curr.next
        
        return copy_dummy.next
    
    
#         ### dict: key = node, val = copy_node ###
#         copy = dict()
        
#         # copy all node.val
#         curr = head
#         while curr:
#             copy[curr] = Node(curr.val)
#             curr = curr.next
        
#         # copy node.next and node.random
#         curr = head
#         while curr:
#             copy_node = copy[curr]
#             copy_node.next = copy.get(curr.next) # curr.next can be None
#             copy_node.random = copy.get(curr.random) # curr.random can be None
#             curr = curr.next
#         copy_head = copy[head]
#         return copy_head
    
#         ### defaultdict ###
#         from collections import defaultdict
        
#         copy = defaultdict(lambda: Node(0)) 
#         copy[None] = None # for curr.next = None or curr.random = None
        
#         curr = head
#         while curr:
#             copy_node = copy[curr] # initialize copy_node
#             copy_node.val = curr.val
#             copy_node.next = copy[curr.next]
#             copy_node.random = copy[curr.random]
#             curr = curr.next      
#         copy_head = copy[head]
#         return copy_head
