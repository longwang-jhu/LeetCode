# https://leetcode.com/problems/3sum/

# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

###############################################################################

# unique triplets -> sort -> fix a -> 2Sum
# sorted -> use ptrs for b and c and move towards middle

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3: return []
        
        n = len(nums)
        nums.sort()
        ans = []
        
        for offset in range(n - 2): # for a = nums[offset]
            if offset > 0 and nums[offset] == nums[offset - 1]: # skip identical a
                continue
            
            # find b + c = -a
            target = - nums[offset]
            # use ptrs for b and c, and move towards middle
            left = offset + 1
            right = n - 1
            
            while left < right:
                total = nums[left] + nums[right]
                if total < target: # b is too small
                    left += 1
                elif total > target: # c is too large
                    right -= 1
                else:
                    ans.append([nums[offset], nums[left], nums[right]])
                    # continue search for b, c
                    while left < right and nums[left] == nums[left + 1]: # skip identical b
                        left += 1
                    left += 1
                                        
                    while left < right and nums[right] == nums[right - 1]: # skip identical c
                        right -= 1
                    right -= 1
        return ans