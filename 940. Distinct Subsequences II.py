# https://leetcode.com/problems/distinct-subsequences-ii/

# Given a string S, count the number of distinct, non-empty subsequences of S .

# Since the result may be large, return the answer modulo 10^9 + 7.

###############################################################################

# dp[i] = number of subseq of S (first i chars)

class Solution:
    def distinctSubseqII(self, S: str) -> int:
        n = len(S)
        dp = [0] * (n + 1)
        dp[0] = 1
        last_appear = {}
        
        for i in range(1, n + 1):
            char = S[i-1]
            dp[i] = dp[i-1] * 2
            
            if char in last_appear:
                dp[i] -= dp[last_appear[char] - 1]
            last_appear[char] = i

        return (dp[-1] - 1) % (10**9 + 7)
        
        
#         n = len(S)
#         dp = [0] * (n + 1)
#         dp[0] = 1 # count empty subseq
        
#         last_appear = {} # use to remove duplicate, key = char, val = i
#         for i in range(1, n + 1):
#             char = S[i-1]
#             dp[i] = dp[i-1] * 2 # expand by appending char to every existing subseq
            
#             # remove duplicate by substracting the prev operation of appending the same char
#             if char in last_appear:
#                 dp[i] -= dp[last_appear[char]]
#             last_appear[char] = i
            
#         return (dp[-1] - 1) % (10**9 + 7) # remove empty subseq