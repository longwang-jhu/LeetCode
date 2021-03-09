# method 1: use stack to store every word between () and reverse it when encounter ')'
# method 2: use Dict to store all paired () and travel as wormhole =>(<- ... <=)->

class Solution:
    def reverseParentheses(self, s: str) -> str:
        # method 1
        # ans = [''] # store words between ()
        # for char in s:
        #     if char == '(':
        #         ans.append('') # create a new position for next word
        #     elif char == ')':
        #         rev_words = ans.pop()[::-1] # reverse the word
        #         ans[-1] += rev_words # combine it with previous word
        #     else:
        #         ans[-1] += char
        # return ''.join(ans)
        
        # method 2
        # find all paired ()
        stack = []
        paren_pair = {}
        for idx, char in enumerate(s):
            if char == '(':
                stack.append(idx)
            elif char == ')':
                left_paren_idx = stack.pop()
                paren_pair[left_paren_idx] = idx
                paren_pair[idx] = left_paren_idx
                
        # travel as wormhold
        ans = []
        curr = 0 # current position
        direction = 1 # direction
        
        while curr < len(s):
            if s[curr] == '(' or s[curr] == ')':
                curr = paren_pair[curr] # jump through wormhold
                direction *= -1
            else:
                ans.append(s[curr])
            curr += direction
        return ''.join(ans)