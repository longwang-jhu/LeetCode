# https://leetcode.com/problems/binary-trees-with-factors/

# Given an array of unique integers, arr, where each integer arr[i] is strictly
# greater than 1.

# We make a binary tree using these integers, and each number may be used for
# any number of times. Each non-leaf node's value should be equal to the
# product of the values of its children.

# Return the number of binary trees we can make. The answer may be too large so
# return the answer modulo 109 + 7.

###############################################################################

# dp[i] = no. of trees with root nums[i]
# dp[i] = dp[left] * dp[right] if i == left * right

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        
        dp = [1] * n
        num_idx_dict = {num: i for i, num in enumerate(arr)} # for fast loop up
        
        for i, num in enumerate(arr):
            # look for arr[left] * arr[right] == num
            for left in range(i):
                if num % arr[left] == 0 and num / arr[left] in num_idx_dict: # found a pair
                    right = num_idx_dict[num / arr[left]]
                    dp[i] += (dp[left] * dp[right]) % (10 ** 9 + 7)
        
        return sum(dp) % (10 ** 9 + 7)
                