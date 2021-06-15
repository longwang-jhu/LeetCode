// https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

// Return the lexicographically smallest subsequence of s that contains all the
// distinct characters of s exactly once.

// Note: This question is the same as 316: https://leetcode.com/problems/remove-
// duplicate-letters/

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    string smallestSubsequence(string s) {
        int n = s.size();
        unordered_map<char, int> lastPos;
        unordered_map<char, bool> added;
        for (int i = 0; i < n; ++i) lastPos[s[i]] = i;
        
        string ans;
        for (int i = 0; i < n; ++i) {
            if (!added[s[i]]) {
                while (!ans.empty() and ans.back() > s[i] and lastPos[ans.back()] > i) {
                    added[ans.back()] = false; ans.pop_back();
                }
                ans += s[i]; added[s[i]] = true;
            }
        }
        return ans;
    }
};
