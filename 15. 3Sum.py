# https://leetcode.com/problems/3sum/

# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.

# Notice that the solution set must not contain duplicate triplets.

###############################################################################

# sort first
# fix a, use two pointers for b and c, and move towards the middle

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        n = len(nums)
        nums.sort()
        res = []
        
        for i in range(n):
            # no repeat for a
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # find b + c = -a
            target = -nums[i]
            # use two pointers for b and c, and move towards the middle
            l = i + 1
            r = n - 1
            
            while l < r:
                total = nums[l] + nums[r]
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # no repeat for b
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                    
                    # no repeat for c
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1

        return res