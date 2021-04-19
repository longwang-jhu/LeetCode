# https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.

###############################################################################

# anagrams -> same char count
# dict: key = ('a' count, ..., 'z' count), value = [anagrams]
# time: O(NK), space: O(NK)

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            s_count = [0] * 26 # for 26 chars
            for char in s:
                s_count[ord(char) - ord('a')] += 1
            ans[tuple(s_count)].append(s) # append to ans
        return ans.values()

# anagrams -> same ordered string
# dict: key = ordered string, value = [anagrams]
# time: O(NKlogK), space: O(NK)

    def sorted_str_key(self, strs):
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()