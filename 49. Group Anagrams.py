# https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.

###############################################################################

# anagrams -> same char count
# dict with key = (26 letters count tuple) and value = anagrams
# time: O(NK), space: O(NK)

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for string in strs:
            count = [0] * 26 # for 26 letters
            for char in string:
                count[ord(char) - ord('a')] += 1
            ans[tuple(count)].append(string)
        return ans.values()

# anagrams -> same ordered string
# dict with key = ordered string and value = anagrams
# time: O(NKlogK), space: O(NK)

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for string in strs:
            ans[tuple(sorted(string))].append(string)
        return ans.values()