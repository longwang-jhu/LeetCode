# https://leetcode.com/problems/implement-queue-using-stacks/

# Implement a first in first out (FIFO) queue using only two stacks. The
# implemented queue should support all the functions of a normal queue (push,
# peek, pop, and empty).

# Implement the MyQueue class:

# Notes:

# Follow-up: Can you implement the queue such that each operation is amortized
# O(1) time complexity? In other words, performing n operations will take overall
# O(n) time even if one of those operations may take longer.

################################################################################

# use stack1 and stack2
# push to stack1, pop from stack2
# when stack2 is empty, borrow ele from stack1

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # if stack2 is not empty, directly pop
        # if stack2 is empty, pop stack1 to append into stack2, and then pop
        
        if not self.stack2: # stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if self.stack2:
            return self.stack2.pop()
        else:
            return None

    def peek(self) -> int:
        """
        Get the front element.
        """
        # similar to pop
        
        if not self.stack2:  # stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if self.stack2:
            return self.stack2[-1]
        else:
            return None
        
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack1 and not self.stack2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
