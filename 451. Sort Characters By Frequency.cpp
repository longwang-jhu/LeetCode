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
        for (char &c : s) ++counts[c];
        
        // bucket[count] = chars with that many count
        vector<vector<char>> bucket(s.size() + 1);
        for (auto &[c, count] : counts) bucket[count].push_back(c);
        
        string ans;
        for (int count = s.size(); count > 0; --count) {
            for (char &c : bucket[count]) ans += string(count, c);
        }
        
        return ans;
    }
};
