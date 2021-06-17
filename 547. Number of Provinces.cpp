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
        n = isConnected.size();
        visited = vector<bool>(n, false);
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                dfs(i, isConnected); ++ans;
            }
        }
        return ans;
    }
private:
    int n;
    vector<bool> visited;
    void dfs(int i, const vector<vector<int>>& isConnected) {
        visited[i] = true;
        for (int j = 0; j < n; ++j) { // generate children
            if (j == i) continue;
            if (!visited[j] && isConnected[i][j] == 1) {
                dfs(j, isConnected);
            }
        }
        return;
    }
};
