// https://leetcode.com/problems/minimum-height-trees/

// A tree is an undirected graph in which any two vertices are connected by exactly
// one path. In other words, any connected graph without simple cycles is a tree.

// Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges
// where edges[i] = [ai, bi] indicates that there is an undirected edge between the
// two nodes ai and bi in the tree, you can choose any node of the tree as the
// root. When you select a node x as the root, the result tree has height h. Among
// all possible rooted trees, those with minimum height (i.e. min(h))  are called
// minimum height trees (MHTs).

// Return a list of all MHTs' root labels. You can return the answer in any order.

// The height of a rooted tree is the number of edges on the longest downward path
// between the root and a leaf.

////////////////////////////////////////////////////////////////////////////////

// toplogical sort, stop when rem nodes <= 2
class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (n == 1) return {0};
        if (n == 2) return {0, 1};
        unordered_map<int, unordered_set<int>> graph;
        for (const auto& edge : edges) {
            graph[edge[0]].insert(edge[1]);
            graph[edge[1]].insert(edge[0]);
        }
        
        queue<int> todo;
        for (int i = 0; i < n; ++i) {
            if (graph[i].size() == 1) todo.push(i);
        }
        while (n > 2) {
            int nCurrLayer = todo.size();
            n -= nCurrLayer;
            while (nCurrLayer--) {
                int node = todo.front(); todo.pop();
                int neigh = *(graph[node].begin());
                graph[node].erase(neigh);
                graph[neigh].erase(node);
                if (graph[neigh].size() == 1) todo.push(neigh);
            }
        }
        vector<int> ans;
        while (!todo.empty()) {
            ans.push_back(todo.front());
            todo.pop();
        }
        return ans;
    }
};
