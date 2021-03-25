# https://leetcode.com/problems/container-with-most-water/

# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
# the x-axis forms a container, such that the container contains the most
# water.

# Notice that you may not slant the container.

###############################################################################

# two pointers from both sides, move the shorter one towards the middle

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res