# https://leetcode.com/problems/reverse-vowels-of-a-string/

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

################################################################################

# use left and right

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        s = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            while s[left] not in vowels and left < right:
                left += 1
            while s[right] not in vowels and left < right:
                right -= 1
            if left < right:
                s[right], s[left] = s[left], s[right]
                left += 1
                right -= 1
        
        return ''.join(s)
