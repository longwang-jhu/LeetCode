# dfs(comb, leftP, rightP), exits when leftP == n and rightP == n

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(comb, leftP, rightP):
            if leftP == n and rightP == n: # exit case
                res.append(comb)
                return
            if leftP < n:
                dfs(comb + "(", leftP + 1, rightP)
            if rightP < leftP: # can only add ")" when there are more "("
                dfs(comb + ")", leftP, rightP + 1)
        
        dfs("", 0, 0)
        return res
    
        res = []
        comb = []
        def dfs(leftP, rightP):
            if leftP == n and rightP == n:
                res.append("".join(comb)) # exit case
            else:
                if leftP < n:
                    comb.append("(")
                    dfs(leftP + 1, rightP)
                    comb.pop()
                if rightP < leftP: # can only add ")" when there are more "("
                    comb.append(")")
                    dfs(leftP, rightP + 1)
                    comb.pop()
        dfs(0,0)
        return res