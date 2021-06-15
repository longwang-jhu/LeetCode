# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.

# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.

# 

###############################################################################

# all combinations -> dfs / bfs
# Dict with key = digit and value = letters

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or len(digits) == 0: return []
        
        digits_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"}
        
        ans = []
        self.dfs(ans, [], 0, digits, digits_dict)
        return ans
        
        # return self.bfs(digits, digits_dict)
        
    def dfs(self, ans, holder, pos, digits, digits_dict):
        if pos == len(digits):
            ans.append(''.join(holder))
            return
        
        for letter in digits_dict[digits[pos]]:
            holder.append(letter)
            self.dfs(ans, holder, pos + 1, digits, digits_dict)
            holder.pop()

    def bfs(self, digits, digits_dict):
        ans = ['']
        for digit in digits:
            new_ans = []
            for ele in ans:
                for letter in digits_dict[digit]:
                    new_ans.append(ele + letter)
            ans = new_ans
        return ans