// https://leetcode.com/problems/minimum-window-substring/

// Given two strings s and t of lengths m and n respectively, return the minimum
// window substring of s such that every character in t (including duplicates) is
// included in the window. If there is no such substring, return the empty string
// "".

// The testcases will be generated such that the answer is unique.

// A substring is a contiguous sequence of characters within the string.

////////////////////////////////////////////////////////////////////////////////

// sliding window
class Solution {
public:
    string minWindow(string s, string t) {
        // record t
        unordered_map<char, int> target;
        for (char &c : t) ++target[c];
        
        // sliding window
        unordered_map<char, int> window;
        
        int minLen = INT_MAX, currLen, startPos;
        char newChar, oldChar;
        int nValid = 0; // number of valid chars
        
        int left = 0, right = 0;
        while (right < s.size()) {
            // update window
            newChar = s[right];
            if (target.find(newChar) != target.end()) {
                ++window[newChar];
                if (window[newChar] == target[newChar]) ++nValid;
            }
            
            // shrink window
            while (nValid == target.size()) {
                // update minLen
                currLen = right - left + 1;
                if (currLen < minLen) {
                    minLen = currLen;
                    startPos = left;
                }
                
                // remove oldChar from window
                oldChar = s[left];
                if (target.find(oldChar) != target.end()) {
                    if (window[oldChar] == target[oldChar]) --nValid;
                    --window[oldChar];
                }
                ++left;
            }
            
            // expand window
            ++right;
        }
        
        if (minLen == INT_MAX) return {};
        return s.substr(startPos, minLen);
    }
};
