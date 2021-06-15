// https://leetcode.com/problems/substring-with-concatenation-of-all-words/

// You are given a string s and an array of strings words of the same length.
// Return all starting indices of substring(s) in s that is a concatenation of each
// word in words exactly once, in any order, and without any intervening
// characters.

// You can return the answer in any order.

////////////////////////////////////////////////////////////////////////////////

// sliding window
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        unordered_map<string, int> target;
        for (string& word : words) ++target[word];
        
        vector<int> ans;
        int n = s.size(), k = words[0].size();
        // check s.substr(offset, m * k) == target
        for (int offset = 0; offset < k; ++offset) {
            // sliding window
            unordered_map<string, int> window;
            int left = offset, right = offset, match = 0;
            while (right + k - 1 < n) {
                string newWord = s.substr(right, k);
                if (target.find(newWord) != target.end()) { // newWord is good
                    ++window[newWord];
                    if (window[newWord] == target[newWord]) ++match;
                } else { // skip bad word, reset window
                    window.clear(); match = 0; right += k; left = right;
                    continue;
                }
                // shrink window
                while (window[newWord] > target[newWord]) {
                    string oldWord = s.substr(left, k);
                    if (window[oldWord] == target[oldWord]) --match;
                    --window[oldWord];
                    left += k;
                }
                if (match == target.size()) ans.push_back(left); // update ans
                right += k; // expand window
            }
        }
        return ans;
    }
};
