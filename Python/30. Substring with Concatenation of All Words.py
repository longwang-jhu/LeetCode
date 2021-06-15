# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

# You are given a string s and an array of strings words of the same length.
# Return all starting indices of substring(s) in s that is a concatenation of
# each word in words exactly once, in any order, and without any intervening
# characters.

# You can return the answer in any order.

###############################################################################

# sliding window, use dict for comparison
# check s[0 : m * k] == words
# move sliding window -> check s[k : m * k + k] == words
# loop over offset in range(k) -> check s[offset : offset + m * k] == words

from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n, m, k = len(s), len(words), len(words[0])
        
        # init words dict
        words_dict = defaultdict(int)
        for word in words:
            words_dict[word] += 1

        ans = []
        running_dict = defaultdict(int)
        for offset in range(k):
            running_dict.clear()
            
            # init sliding window
            left, right = offset, offset + m * k
            if right > n: return ans
            
            for i in range(left, right, k):
                word = s[i : i + k]
                running_dict[word] += 1
            
            if running_dict == words_dict:
                ans.append(left)

            # move sliding window
            for i in range(right, n, k):
                next_word = s[i : i + k]
                prev_word = s[i - m * k : i - m * k + k]
                
                running_dict[next_word] += 1
                running_dict[prev_word] -= 1
                if running_dict[prev_word] == 0:
                    running_dict.pop(prev_word)
                
                if running_dict == words_dict:
                    ans.append(i - m * k + k)
        
        return ans