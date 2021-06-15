// https://leetcode.com/problems/loud-and-rich/

// In a group of N people (labelled 0, 1, 2, ..., N-1), each person has different
// amounts of money, and different levels of quietness.

// For convenience, we'll call the person with label x, simply "person x".

// We'll say that richer[i] = [x, y] if person x definitely has more money than
// person y.  Note that richer may only be a subset of valid observations.

// Also, we'll say quiet[x] = q if person x has quietness q.

// Now, return answer, where answer[x] = y if y is the least quiet person (that is,
// the person y with the smallest value of quiet[y]), among all people who
// definitely have equal to or more money than person x.

////////////////////////////////////////////////////////////////////////////////

// edge x -> y if y is richer, for each x look for the quietest person start from x
class Solution {
public:
    // graph[x] = set of richer people
    unordered_map<int, unordered_set<int>> graph;
    vector<int> ans;
    vector<int> loudAndRich(vector<vector<int>>& richer, vector<int>& quiet) {
        for (auto& edge : richer) graph[edge[1]].insert(edge[0]);
        
        ans = vector<int>(quiet.size(), -1);
        for (int i = 0; i < quiet.size(); ++i) dfs(quiet, i);
        return ans;
    }
    
    int dfs(const vector<int>& quiet, int i) {
        if (ans[i] != -1) return ans[i];
        ans[i] = i; // initial val
        for (auto child : graph[i]) {
            int childAns = dfs(quiet, child);
            if (quiet[childAns] < quiet[ans[i]]) ans[i] = childAns;
        }
        return ans[i];
    }
};
