# https://leetcode.com/problems/sort-characters-by-frequency/

# Given a string s, sort it in decreasing order based on the frequency of
# characters, and return the sorted string.

###############################################################################

# bucket sort
# bucket[count] = char

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        
        bucket = [[] for _ in range(len(s) + 1)]
        for char, count in counts.items():
            bucket[count].append(char)
        
        ans = ''
        for count in range(len(bucket))[::-1]:
            if bucket[count]:
                for char in bucket[count]:
                    ans += char * count
        
        return ans