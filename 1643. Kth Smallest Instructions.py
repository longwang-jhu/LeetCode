# https://leetcode.com/problems/kth-smallest-instructions/

# Bob is standing at cell (0, 0), and he wants to reach destination: (row,
# column). He can only travel right and down. You are going to help Bob by
# providing instructions for him to reach destination.

# The instructions are represented as a string, where each character is either:

# Multiple instructions will lead Bob to destination. For example, if destination
# is (2, 3), both "HHHVV" and "HVHVH" are valid instructions.

# However, Bob is very picky. Bob has a lucky number k, and he wants the kth
# lexicographically smallest instructions that will lead him to destination. k is
# 1-indexed.

# Given an integer array destination and an integer k, return the kth
# lexicographically smallest instructions that will take Bob to destination.

################################################################################

# find the kth element in full combination of "H" and "V"
# assume append "V" and count how many elements would be skipped ([H|...])

from math import comb
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        V_total, H_total = destination[0], destination[1]
        
        ans = []
        # sequentially decide if can append "V"
        V_unused = V_total
        for i in range(V_total + H_total): # loop over every step
            if V_unused == 0:
                ans.append("H")
                continue
            
            # check if can append "V"
            # count skipped elements [H|...]
            n_skipped = comb(V_total + H_total - (i + 1), V_unused)
            if n_skipped < k: # OK to append "V"
                ans.append("V")
                V_unused -= 1
                k -= n_skipped
            else: # cannot append "V"
                ans.append("H")

        return ''.join(ans)
