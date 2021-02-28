# use dfs or bfs

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        digitToLetterDict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"}
             
        # dfs
        # def dfs(idx: int):
        #     if idx == len(digits): # reach the end
        #         res.append("".join(letterComb))
        #     else:
        #         digit = digits[idx]
        #         for letter in digitToLetterDict[digit]:
        #             letterComb.append(letter) # go to child
        #             dfs(idx + 1)
        #             letterComb.pop() # go back to parent
        # res = []
        # letterComb = []
        # dfs(0)
        # return res
        
        # bfs - simple
        # res = [""]
        # for digit in digits:
        #     new_res = []
        #     for letterComb in res:
        #         for letter in digitToLetterDict[digit]:       
        #             # add a new letter
        #             new_res.append(letterComb + letter)
        #     res = new_res
        # return res
        
        # bfs - recursive
        def bfs(idx: int):
            if idx == len(digits): # reach the end
                return
            else:
                digit = digits[idx]
                new_res = []
                for letterComb in res:
                    for letter in digitToLetterDict[digit]:
                        new_res.append(letterComb + letter)              
                res.clear()
                res.extend(new_res)
                bfs(idx + 1)
        
        res = [""]
        bfs(0)
        return res