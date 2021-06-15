# stack with in order

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.curr = root
        self.stack = []

    def next(self) -> int:
        while self.curr: # go all the way to the left
            self.stack.append(self.curr)
            self.curr = self.curr.left
        
        node = self.stack.pop()
        self.curr = node.right
        return node.val

    def hasNext(self) -> bool:
        return self.curr != None or len (self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()