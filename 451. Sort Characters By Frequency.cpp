// https://leetcode.com/problems/sort-characters-by-frequency/

// Given a string s, sort it in decreasing order based on the frequency of
// characters, and return the sorted string.

////////////////////////////////////////////////////////////////////////////////

// bucket sort, bucket[count] = chars with that many count
class Solution {
public:
    string frequencySort(string s) {
        // counts[char] = count of char
        unordered_map<char, int> counts;
        int maxCount = 0;
        for (const auto& c : s) {
            maxCount = max(maxCount, ++counts[c]);
        }
        // bucket[count] = chars with that many count
        vector<vector<char>> bucket(maxCount + 1);
        for (const auto& [c, count] : counts) bucket[count].push_back(c);
        string ans;
        for (int i = maxCount; i > 0; --i) {
            for (const auto& c : bucket[i]) ans += string(i, c);
        }
        return ans;
    }
};
