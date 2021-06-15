# https://leetcode.com/problems/reverse-vowels-of-a-string/

# Write a function that takes a string as input and reverse only the vowels of
# a string.

# Example 1:

# Example 2:

# Note: The vowels does not include the letter "y".

###############################################################################

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