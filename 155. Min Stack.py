# https://leetcode.com/problems/min-stack/

# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.

# Implement the MinStack class:

###############################################################################

# use stack
# use min_stack to record the minimum value

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [] # store minimum value
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(self.min_stack[-1], val))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()