# https://leetcode.com/problems/largest-rectangle-in-histogram/

# Given an array of integers heights representing the histogram's bar height where
# the width of each bar is 1, return the area of the largest rectangle in the
# histogram.

################################################################################

# for each ele, find the frist ele on left and right that is smaller
# use stack to find numbers faster

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1: return heights[0]
                
        heights.append(0) # for popping all prev ele
        ans = 0
        stack = [0] # store idx
        
        for i in range(1, len(heights)):
            while stack and heights[stack[-1]] > heights[i]: # pop the prev bar since found its right limit
                idx = stack.pop() # calculate area of this bar
                height = heights[idx]
                
                if stack:
                    prev_idx = stack[-1]
                else:
                    prev_idx = - 1
                    
                width = i - prev_idx - 1 # left limit idx = prev_idx, right limit idx = i
                ans = max(ans, height * width)
            stack.append(i)
        return ans
