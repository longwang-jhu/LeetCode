# https://leetcode.com/problems/remove-invalid-parentheses/

# Given a string s that contains parentheses and letters, remove the minimum
# number of invalid parentheses to make the input string valid.

# Return all the possible results. You may return the answer in any order.

################################################################################

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        leftExtra = rightExtra = 0
        for c in s:
            if c == "(":
                leftExtra += 1
            elif c == ")":
                if leftExtra == 0:
                    rightExtra += 1
                else:
                    leftExtra -= 1
        self.s = s;
        self.ans = set()
        self.holder = [];
        self.dfs(leftExtra, rightExtra, 0, 0, 0)
        return list(self.ans)
    
    def dfs(self, leftExtra, rightExtra, leftCount, rightCount, idx):
        if idx == len(self.s):
            if leftExtra == rightExtra == 0:
                self.ans.add("".join(self.holder))
            return

        if self.s[idx] == "(":
            if leftExtra > 0:
                self.dfs(leftExtra - 1, rightExtra, leftCount, rightCount, idx + 1)
            self.holder.append("(")
            self.dfs(leftExtra, rightExtra, leftCount + 1, rightCount, idx + 1)
            self.holder.pop();
        elif self.s[idx] == ")":
            if rightExtra > 0:
                self.dfs(leftExtra, rightExtra - 1, leftCount, rightCount, idx + 1)
            if leftCount > rightCount:
                self.holder.append(")")
                self.dfs(leftExtra, rightExtra, leftCount, rightCount + 1, idx + 1)
                self.holder.pop()
        else:
            self.holder.append(self.s[idx])
            self.dfs(leftExtra, rightExtra, leftCount, rightCount, idx + 1)
            self.holder.pop()
