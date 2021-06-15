// https://leetcode.com/problems/longest-common-prefix/

// Write a function to find the longest common prefix string amongst an array of
// strings.

// If there is no common prefix, return an empty string "".

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 1) return strs[0];
        string ans;
        for (int i = 0; i < strs[0].size(); ++i) {
            char s = strs[0][i];
            for (int j = 1; j < strs.size(); ++j) {
                if (i >= strs[j].size() or s != strs[j][i]) return ans;
            }
            ans += s;
        }
        return ans;
    }
};
