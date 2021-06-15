// https://leetcode.com/problems/partition-labels/

// You are given a string s. We want to partition the string into as many parts as
// possible so that each letter appears in at most one part.

// Return a list of integers representing the size of these parts.

////////////////////////////////////////////////////////////////////////////////

// greedy, get lastPos of each char
class Solution {
public:
    vector<int> partitionLabels(string s) {
        if (s.empty()) return {};
        if (s.size() == 1) return vector<int>(1,1);
        
        // lastPos[char] = latest index of char
        unordered_map<char, int> lastPos;
        for (int i = 0; i < s.size(); ++i) lastPos[s[i]] = i;
        
        vector<int> ans;
        int anchor = 0, frontier = 0;
        for (int i = 0; i < s.size(); ++i) {
            char c = s[i];
            // keep updating frontier
            frontier = max(frontier, lastPos[c]);
            if (i == frontier) {
                ans.push_back(frontier - anchor + 1);
                anchor = frontier + 1;
            }
        }
        return ans;
    }
};
