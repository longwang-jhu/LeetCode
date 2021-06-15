# https://leetcode.com/problems/number-of-1-bits/

# Write a function that takes an unsigned integer and returns the number of '1'
# bits it has (also known as the Hamming weight).

# Note:

################################################################################

# use n & 1 to see if last bit is 1
# use n >> 1 to shift bit to right


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1 # get last bit
            n >>= 1 # shift bit to right
        return count
            
