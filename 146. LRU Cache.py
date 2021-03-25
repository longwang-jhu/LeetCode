# https://leetcode.com/problems/lru-cache/

# Design a data structure that follows the constraints of a Least Recently Used
# (LRU) cache.

# Implement the LRUCache class:

# Follow up: Could you do get and put in O(1) time complexity?

###############################################################################

# orderedDict = dict + doubly linked list

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key) # update to latest
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        else:
            self.cache.move_to_end(key)
        
        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)