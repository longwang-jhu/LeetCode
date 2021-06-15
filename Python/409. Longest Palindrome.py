# https://leetcode.com/problems/longest-palindrome/

# Given a string s which consists of lowercase or uppercase letters, return the
# length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome
# here.

###############################################################################

# count char times
# ans += count // 2 * 2
# add middle char at the end

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_counts = {}
        for char in s:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        
        ans = 0
        for count in char_counts.values():
            ans += count // 2 * 2
        
        if ans < len(s): # for the middle char
            ans += 1
        return ans