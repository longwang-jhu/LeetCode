# sort first
# fix a, b, use two pointers for c and d, and move towards the middle

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        
        n = len(nums)   
        nums.sort()
        res = []
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i-1]: # no repeat for a
                continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j-1]: # no repeat for b
                    continue
                
                # find c + d = a + b
                l = j + 1
                r = n - 1
                
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total < target:
                        l += 1
                    elif total > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        
                        # no repeat for c
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        l += 1
                        
                        # no repeat for d
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        r-= 1
                        
        return res