# just reverse each word

class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        s = list(s)
        l = 0
        while l < len(s):
            # find the right index of a word
            r = l + 1
            while r < len(s) and s[r] != ' ': # word ends at r - 1
                r += 1
            s[l:r] = s[l:r][::-1] # reverse the word
            l = r + 1 # move to the next word
        
        return ''.join(s)