# https://leetcode.com/problems/product-of-array-except-self/

# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.

###############################################################################

# compute pre_prod and post_prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # compute prefix product
        pre_prod = [1] * n
        for i in range(1, n):
            pre_prod[i] = pre_prod[i - 1] * nums[i - 1]
        
        # compute postfix product
        post_prod = [1] * n
        for i in range(n - 2, -1, -1):
            post_prod[i] = post_prod[i + 1] * nums[i + 1]
        
        # combine
        ans = [1] * n
        for i in range(n):
            ans[i] = pre_prod[i] * post_prod[i]
        
        return ans