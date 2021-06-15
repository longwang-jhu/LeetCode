# https://leetcode.com/problems/can-place-flowers/

# You have a long flowerbed in which some of the plots are planted, and some are
# not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and
# 1 means not empty, and an integer n, return if n new flowers can be planted in
# the flowerbed without violating the no-adjacent-flowers rule.

################################################################################

# greedy

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        if not flowerbed: return False
        
        ans = 0
        curr = 0
        while curr < len(flowerbed):
            # check left and right
            if flowerbed[curr] == 0 \
            and (curr == 0 or flowerbed[curr - 1] == 0) \
            and (curr == len(flowerbed) - 1 or flowerbed[curr + 1] == 0):
                flowerbed[curr] = 1
                ans += 1
            curr += 1
        
        return ans >= n
