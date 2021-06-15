# https://leetcode.com/problems/candy/

# There are n children standing in a line. Each child is assigned a rating value
# given in the integer array ratings.

# You are giving candies to these children subjected to the following
# requirements:

# Return the minimum number of candies you need to have to distribute the candies
# to the children.

################################################################################

# greedy: init [1...1]
# one scan to right
# one scan to left

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings: return 0
        n = len(ratings)
        if n == 1: return 1
        
        ans = [1] * n
        # scan to right
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                ans[i] = ans[i-1] + 1
        # scan to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                ans[i] = max(ans[i], ans[i+1] + 1)

        return sum(ans)
