# https://leetcode.com/problems/queue-reconstruction-by-height/

# You are given an array of people, people, which are the attributes of some
# people in a queue (not necessarily in order). Each people[i] = [hi, ki]
# represents the ith person of height hi with exactly ki other people in front
# who have a height greater than or equal to hi.

# Reconstruct and return the queue that is represented by the input array
# people. The returned queue should be formatted as an array queue, where
# queue[j] = [hj, kj] is the attributes of the jth person in the queue
# (queue[0] is the person at the front of the queue).

###############################################################################

# tallest first (sort by k)
# insert second heightest based on k val

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        for p in people:
            k = p[1]
            ans.insert(k, p)
        
        return ans