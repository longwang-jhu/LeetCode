# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] =
# [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is,
# one domino can be rotated to be equal to another domino.

# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and
# dominoes[i] is equivalent to dominoes[j].

###############################################################################

# use dict with key = min(d[0], d[1]) * 10 + max(d[0], d[1])

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        domino_dict = {}
        for d in dominoes:
            key = min(d[0], d[1]) * 10 + max(d[0], d[1])
            if key in domino_dict:
                domino_dict[key] += 1
            else:
                domino_dict[key] = 1
        
        ans = 0
        for value in domino_dict.values():
            ans += value * (value - 1) / 2
        
        return int(ans)