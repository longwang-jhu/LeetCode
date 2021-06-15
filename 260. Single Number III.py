# https://leetcode.com/problems/single-number-iii/

# Given an integer array nums, in which exactly two elements appear only once and
# all the other elements appear exactly twice. Find the two elements that appear
# only once. You can return the answer in any order.

# You must write an algorithm that runs in linear runtime complexity and uses only
# constant extra space.

################################################################################

# XOR all num to get (a XOR b)
# get LSB of (a XOR b) to seperate data in two groups

# LSB (rightmost 1-bit): x & -x OR x & (~x + 1)
# MSB (leftmost 1-bit): 1 << (x.bit_length() - 1)

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a_xor_b = 0
        for num in nums:
            a_xor_b ^= num
        
        # get LSB
        lsb = a_xor_b & -a_xor_b

        # get ans by seperate data into two groups
        ans = [0, 0]
        for num in nums:
            if num & lsb:
                ans[0] ^= num
            else:
                ans[1] ^= num
        
        return ans
