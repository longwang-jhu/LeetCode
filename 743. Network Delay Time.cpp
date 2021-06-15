// https://leetcode.com/problems/network-delay-time/

// You are given a network of n nodes, labeled from 1 to n. You are also given
// times, a list of travel times as directed edges times[i] = (ui, vi, wi), where
// ui is the source node, vi is the target node, and wi is the time it takes for a
// signal to travel from source to target.

// We will send a signal from a given node k. Return the time it takes for all the
// n nodes to receive the signal. If it is impossible for all the n nodes to
// receive the signal, return -1.

////////////////////////////////////////////////////////////////////////////////

// time: O(N^2 + E), or O(ElogE) is using heap
// space: O(N + E)

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        return networkDelayTimeHeap(times, n, k);
        // graph[node] = {(neigh, weight)}
        vector<vector<pair<int, int>>> graph(n);
        for (auto& edge : times) graph[edge[0]-1].push_back(make_pair(edge[1]-1, edge[2]));
        
        vector<int> dists(n, INT_MAX); dists[k-1] = 0; // dists[node] = distance to node
        vector<bool> visited(n, false);        
        while (true) {
            // find unvisited node with smallest dist
            int node = -1, dist = INT_MAX;
            for (int cand = 0; cand < n; ++cand) {
                if (!visited[cand] and dists[cand] < dist) {
                    node = cand; dist = dists[cand];
                }
            }
            if (node == -1) break; // cannot find any node
            visited[node] = true;
            for (auto& [neigh, weight] : graph[node]) {
                dists[neigh] = min(dists[neigh], dists[node] + weight);
            }
        }
        int distMax = *max_element(dists.begin(), dists.end());
        return distMax == INT_MAX ? -1 : distMax;
    }
    
    int networkDelayTimeHeap(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int, int>>> graph(n);
        for (auto& edge : times) graph[edge[0]-1].push_back(make_pair(edge[1]-1, edge[2]));
        
        vector<int> dists(n, INT_MAX); // dists[node] = distance to node
        vector<bool> visited(n, false);
        // min-pq = {(dist to node, node)}
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> todo;
        todo.push(make_pair(0, k-1));
        while (!todo.empty()) {
            auto [dist, node] = todo.top(); todo.pop();
            if (!visited[node]) {
                dists[node] = dist; visited[node] = true;
                for (auto& [neigh, weight] : graph[node]) {
                    todo.push(make_pair(dists[node] + weight, neigh));
                }
            }
        }
        int distMax = *max_element(dists.begin(), dists.end());
        return distMax == INT_MAX ? -1 : distMax;
   }
};
