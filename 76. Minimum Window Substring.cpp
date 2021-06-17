// https://leetcode.com/problems/minimum-window-substring/

// Given two strings s and t of lengths m and n respectively, return the minimum
// window substring of s such that every character in t (including duplicates) is
// included in the window. If there is no such substring, return the empty string
// "".

// The testcases will be generated such that the answer is unique.

// A substring is a contiguous sequence of characters within the string.

////////////////////////////////////////////////////////////////////////////////

// sliding window, use hashMap for comparison
class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> window, target;
        for (const auto& c : t) ++target[c];
        
        int minLen = INT_MAX, i, left = 0, right = 0, nValid = 0;
        for (int left = 0, right = 0; right < s.size(); ++right) {
            // update window
            char newChar = s[right];
            if (target.find(newChar) != target.end()) {
                ++window[newChar];
                if (window[newChar] == target[newChar]) ++nValid;
            }
            // shrink window
            while (nValid == target.size()) {
                // update minLen
                int currLen = right - left + 1;
                if (minLen > currLen) {
                    minLen = currLen; i = left;
                }
                char oldChar = s[left];
                if (target.find(oldChar) != target.end()) {
                    if (window[oldChar] == target[oldChar]) --nValid;
                    --window[oldChar];
                }
                ++left;
            }
        }
        if (minLen == INT_MAX) return {};
        return s.substr(i, minLen);
    }
};
