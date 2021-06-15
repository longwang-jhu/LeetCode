# https://leetcode.com/problems/majority-element-ii/

# Given an integer array of size n, find all elements that appear more than ⌊ n/3
# ⌋ times.

# Follow-up: Could you solve the problem in linear time and in O(1) space?

################################################################################

# offset whenevery three numbers are different
# recount after finding majority nums to make sure count > n // 3

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans1, ans2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if num == ans1:
                count1 += 1
            elif num == ans2:
                count2 += 1
            elif count1 == 0:
                ans1 = num
                count1 += 1
            elif count2 == 0:
                ans2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1, count2 = 0, 0
        for num in nums:
            if num == ans1:
                count1 += 1
            elif num == ans2:
                count2 += 1
        
        min_count = len(nums) // 3
        if count1 > min_count and count2 > min_count:
            return [ans1, ans2]
        elif count1 > min_count:
            return [ans1]
        elif count2 > min_count:
            return [ans2]
