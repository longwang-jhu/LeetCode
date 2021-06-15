# https://leetcode.com/problems/partition-labels/

# You are given a string s. We want to partition the string into as many parts as
# possible so that each letter appears in at most one part.

# Return a list of integers representing the size of these parts.

################################################################################

# greedy -> find last idx of each char -> check when can make a partition

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S: return []
        if len(S) == 1: return [1]
        
        char_last_idx = {char: idx for idx, char in enumerate(S)}
        
        anchor = frontier = 0
        ans = []
        for i, char in enumerate(S):
            # keep updating partition pos
            frontier = max(frontier, char_last_idx[char])
            if i == frontier: # can make a partition
                ans.append(i - anchor + 1)
                anchor = i + 1
        
        return ans
