// https://leetcode.com/problems/number-of-provinces/

// There are n cities. Some of them are connected, while some are not. If city a is
// connected directly with city b, and city b is connected directly with city c,
// then city a is connected indirectly with city c.

// A province is a group of directly or indirectly connected cities and no other
// cities outside of the group.

// You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith
// city and the jth city are directly connected, and isConnected[i][j] = 0
// otherwise.

// Return the total number of provinces.

////////////////////////////////////////////////////////////////////////////////

// dfs
class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int ans = 0;
        vector<bool> visited(isConnected.size(), false);
        for (int i = 0; i < isConnected.size(); ++i) {
            if (!visited[i]) {
                dfs(isConnected, visited, i);
                ++ans;
            }
        }
        return ans;
    }
    
    void dfs(const vector<vector<int>> &isConnected,
             vector<bool> &visited, int i) {
        visited[i] = true;
        // generate children
        for (int j = 0; j < isConnected.size(); ++j) {
            if (j != i and !visited[j] and isConnected[i][j] == 1) {
                dfs(isConnected, visited, j);
            }
        }
        return;
    }
};
