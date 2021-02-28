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