# https://leetcode.com/problems/largest-palindrome-product/

# Given an integer n, return the largest palindromic integer that can be
# represented as the product of two n-digits integers. Since the answer can be
# very large, return it modulo 1337.

################################################################################

# construct 2n-digits (and 2n-1-digits) palin from larges to small
# check if can be a prodct of two n-digits number

class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1: return 9
        
        n_digits_max = 10 ** n - 1 # n-digits: 9...9
        n_digits_min = 10 ** (n - 1) # n-1 digits: 10...0
        
        # loop over every 2n-digits palin
        for left_part in range(n_digits_max, n_digits_min - 1, -1):
            right_part_str = ''.join(list(str(left_part))[::-1])
            palin = int(str(left_part) + right_part_str)
        
            # check product
            for div1 in range(n_digits_max, n_digits_min - 1, -1):
                div2, rem = divmod(palin, div1)
                # check if div2 is n-digits
                if rem == 0 and n_digits_min <= div2 <= n_digits_max:
                    return palin % 1337
        
        return
