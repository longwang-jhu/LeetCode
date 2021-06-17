// https://leetcode.com/problems/word-break/

// Given a string s and a dictionary of strings wordDict, return true if s can be
// segmented into a space-separated sequence of one or more dictionary words.

// Note that the same word in the dictionary may be reused multiple times in the
// segmentation.

////////////////////////////////////////////////////////////////////////////////

// dp[i] = if can break using s[0...i-1]
// to update dp[i], check if s[j...i-1] is word and dp[j] == True
// speed up: stop when len(s[j...i-1]) > max_word_len
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int maxLen = 0;
        unordered_set<string> wordsSet;
        for (const auto& word : wordDict) {
            maxLen = max(maxLen, (int) word.size());
            wordsSet.insert(word);
        }
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;
        for (int i = 1; i <= s.size(); ++i) {
            for (int j = i - 1; j >= 0 && i - j <= maxLen; --j) {
                string word = s.substr(j, i - j);
                if (dp[j] && wordsSet.find(word) != wordsSet.end()) {
                    dp[i] = true; break;
                }
            }
        }
        return dp.back();
    }
};
