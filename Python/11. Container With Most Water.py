# https://leetcode.com/problems/container-with-most-water/

# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
# the x-axis forms a container, such that the container contains the most
# water.

# Notice that you may not slant the container.

###############################################################################

# greedy: two ptrs move towards middle -> move the shorter one (hope to improve)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height or len(height) == 1: return 0

        # two pointers move towards the middle
        left, right = 0, len(height) - 1
        ans = 0
        
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            ans = max(ans, area)
            
            # move the shorter one
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans