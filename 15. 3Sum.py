# https://leetcode.com/problems/3sum/

# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

###############################################################################

# unique triplets -> sort -> fix a -> 2Sum
# since sorted, use pointers for b and c and move towards the middle

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3: return []
        
        n = len(nums)
        nums.sort()
        ans = []
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]: # skip identical a
                continue
            
            # find b + c = -a
            target = -nums[i]
            # use pointers for b and c, and move towards the middle
            l = i + 1
            r = n - 1
            
            while l < r:
                total = nums[l] + nums[r]
                if total < target: # b is too small
                    l += 1
                elif total > target: # c is too large
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    # continue search for b, c
                    # skip identical b
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                    
                    # skip identical c
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
        return ans