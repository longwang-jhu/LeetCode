# remove extra space, reverse entire string, reverse each word
class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        s = list(s)
        
        # remove extra space
        for i in range(len(s) - 1, 0, -1):
            if s[i] == " " and s[i-1] == " ":
                del s[i]
        if s[-1] == " ":
            del s[-1]
        if s[0] == " ":
            del s[0]
        
        s = s[::-1] # reverse entire list
        
        # reverse each words
        l = 0
        while l < len(s):
            while l < len(s) and s[l] == ' ': # find the left index of a word
                l += 1
            if l == len(s):
                break
                
            r = l + 1
            while r < len(s) and s[r] != ' ': # find the right index of a word
                r += 1
                
            s[l:r] = s[l:r][::-1] # reverse the word           
            l = r + 1
        
        return ''.join(s)