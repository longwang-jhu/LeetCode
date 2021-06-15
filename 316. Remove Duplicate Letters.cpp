// https://leetcode.com/problems/remove-duplicate-letters/

// Given a string s, remove duplicate letters so that every letter appears once and
// only once. You must make sure your result is the smallest in lexicographical
// order among all possible results.

////////////////////////////////////////////////////////////////////////////////

// sequentially add non-added char (use hashMap to record), pop prev char if
// i) new char is smaller and ii) can add back prev char later (use hashMap to record lastPos of each char)
class Solution {
public:
    string removeDuplicateLetters(string s) {
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
