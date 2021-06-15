// https://leetcode.com/problems/longest-substring-without-repeating-characters/

// Given a string s, find the length of the longest substring without repeating
// characters.

////////////////////////////////////////////////////////////////////////////////

// sliding window
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() == 0) return 0;
        // window[char] = count
        unordered_map<char, int> window;
        int maxLen = 0, left = 0, right = 0;       
        while (right < s.size()) {
            // update window
            char newChar = s[right];
            ++window[newChar];
            // shrink window
            while (window[newChar] > 1) {
                char oldChar = s[left];
                --window[oldChar];
                ++left;
            }
            // update maxLen
            maxLen = max(maxLen, right - left + 1);
            ++right;
        }
        return maxLen;
    }
};
