# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

# Given a binary string s and an integer k.

# Return true if every binary code of length k is a substring of s. Otherwise,
# return false.

################################################################################

# check every substring of len = k unitl all 2**k binary code are visited
# time: O(nk), space: O(nk)

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return self.use_hash_val(s, k)
        
        if not s: return False
        
        n = len(s)
        codes_visited = set()
        
        for i in range(n - k + 1): # stop at i = n - k
            substr = s[i : i + k]
            codes_visited.add(substr)
            if len(codes_visited) == 2 ** k:
                return True
        
        return False
    
# directly compute hash value of substr
# get new_hash_val from old_hash_val by removing (old) first digit and append (new) last digit

    def use_hash_val(self, s, k):
        need = 1 << k
        codes_visited = [False] * need
        
        all_one = need - 1
        hash_val = 0

        for i in range(len(s)):
            # update hash
            hash_val = ((hash_val << 1) & all_one) | (int(s[i]))
            
            # wait until substr len = k
            if i >= k - 1 and codes_visited[hash_val] is False:
                codes_visited[hash_val] = True
                need -= 1
                
                if need == 0:
                    return True
        
        return False
