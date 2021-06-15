# https://leetcode.com/problems/assign-cookies/

# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie.

# Each child i has a greed factor g[i], which is the minimum size of a cookie that
# the child will be content with; and each cookie j has a size s[j]. If s[j] >=
# g[i], we can assign the cookie j to the child i, and the child i will be
# content. Your goal is to maximize the number of your content children and output
# the maximum number.

################################################################################

# give the smallest cookie to the smallest child

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        ans = 0
        g_idx, s_idx = 0, 0
        while g_idx < len(g) and s_idx < len(s):
            if g[g_idx] <= s[s_idx]:
                g_idx += 1
                ans += 1
            s_idx += 1

        return ans
