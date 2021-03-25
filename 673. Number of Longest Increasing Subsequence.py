# https://leetcode.com/problems/number-of-longest-increasing-subsequence/

# Given an integer array nums, return the number of longest increasing
# subsequences.

# Notice that the sequence has to be strictly increasing.

###############################################################################

# dp_len[i] = length of longest increasing subseq ending at i
# dp_count[i] = count of longest increasing subseq ending at i
# update by checking all prev dp_len[j] such that nums[j] < nums[i]
# update dp_count[i] correspondingly

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        dp_len = [1 for _ in range(n)]
        dp_count = [1 for _ in range(n)]
        for right in range(1,n):
            for left in range(right): # from 0 to right - 1
                if nums[left] < nums[right]: # could extend len
                    if dp_len[left] + 1 == dp_len[right]: # no change to len, increase count
                        dp_count[right] += dp_count[left]
                    if dp_len[left] + 1 > dp_len[right]: # increase len, reset count
                        dp_len[right] = dp_len[left] + 1
                        dp_count[right] = dp_count[left]
        
        # find all the counts
        max_len = max(dp_len)
        ans = 0
        for i, v in enumerate(dp_len):
            if v == max_len:
                ans += dp_count[i]
        return ans
