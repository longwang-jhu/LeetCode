# https://leetcode.com/problems/keyboard-row/

# Given an array of strings words, return the words that can be typed using
# letters of the alphabet on only one row of American keyboard like the image
# below.

# In the American keyboard:

###############################################################################

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        if not words: return []
        
        char_row_dict = dict()
        for char in 'qwertyuiop':
            char_row_dict[char] = 1
        for char in 'asdfghjkl':
            char_row_dict[char] = 2
        for char in 'zxcvbnm':
            char_row_dict[char] = 3
        
        ans = []
        for word in words:
            if len(word) == 1:
                ans.append(word)
            else:
                row_num = char_row_dict[word[0].lower()]
                for char in word:
                    if char_row_dict[char.lower()] != row_num:
                        break
                else:
                    ans.append(word)
        
        return ans