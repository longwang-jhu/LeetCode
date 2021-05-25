# https://leetcode.com/problems/majority-element/

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You
# may assume that the majority element always exists in the array.

###############################################################################

# offset majority num with any other num

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = None
        count = 0
        
        for num in nums:
            if num == ans:
                count += 1
            elif count == 0: # make num as the majority num
                ans = num
            else:
                count -= 1 # offset majority num count by 1
        
        return ans