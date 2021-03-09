# use left and right

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s = list(S)
        left, right = 0, len(s) - 1
        
        while left < right:
            while not s[left].isalpha() and left < right:
                left += 1
            while not s[right].isalpha() and left < right:
                right -= 1
            if left < right:
                s[right], s[left] = s[left], s[right]
                left += 1
                right -= 1
        
        return ''.join(s)