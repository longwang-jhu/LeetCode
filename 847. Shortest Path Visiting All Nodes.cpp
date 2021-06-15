// https://leetcode.com/problems/shortest-path-visiting-all-nodes/

// You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You
// are given an array graph where graph[i] is a list of all the nodes connected
// with node i by an edge.

// Return the length of the shortest path that visits every node. You may start and
// stop at any node, you may revisit nodes multiple times, and you may reuse edges.

////////////////////////////////////////////////////////////////////////////////

// bfs
class Solution {
public:
    int shortestPathLength(vector<vector<int>>& graph) {
        int n = graph.size();
        int target = (1 << n) - 1; // use 1...1 to represent all visited
        
        // queue<current node, current visited state (in binary, 2^n cases)>
        queue<pair<int, int>> q;
        // visited[i][j] = if node i has been visited in state j (in binary, 2^n cases)
        vector<vector<bool>> visited(n, vector<bool>(1 << n, false));
        for (int i = 0; i < n; i++) {
            q.push({i, 1 << i});
            visited[i][1 << i] = true;
        }
        
        int ans = 0;
        while (!q.empty()) {
            int thisSize = q.size();
            for (int i = 0; i < thisSize; ++i){
                auto curr = q.front();
                q.pop();
                int node = curr.first;
                int state = curr.second;
                
                if (state == target) return ans;
                for (int next : graph[node]) {
                    // skip if next has been visited in current state
                    if (visited[next][state]) continue;
                    visited[next][state] = true;
                    q.push({next, state | 1 << next});
                }
            }
            ++ans;
        }
        return ans;
    }
};
