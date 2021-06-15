// https://leetcode.com/problems/jump-game-iv/

// Given an array of integers arr, you are initially positioned at the first index
// of the array.

// In one step you can jump from index i to index:

// Return the minimum number of steps to reach the last index of the array.

// Notice that you can not jump outside of the array at any time.

////////////////////////////////////////////////////////////////////////////////

// bfs with hashMap to record idxes of the same num
class Solution {
public:
    int minJumps(vector<int>& arr) {
        if (arr.size() == 1) return 0;
        
        int n = arr.size();
        unordered_map<int, vector<int>> numIdxes;
        for (int i = 0; i < n; ++i) numIdxes[arr[i]].push_back(i);
        
        queue<int> todo; todo.push(0);
        vector<bool> visited(n, false); visited[0] = true;
        int nLayers = 0;
        while (!todo.empty()) {
            int nThisLayer = todo.size();
            while (nThisLayer--) {
                int curr = todo.front(); todo.pop();
                for (int step : {-1, 1}) {
                    int next = curr + step;
                    if (next == n - 1) return nLayers + 1;
                    if (next >= 0 and next < n and !visited[next]) {
                        todo.push(next);
                        visited[next] = true;
                    }
                }
                for (int next : numIdxes.at(arr[curr])) {
                    if (next == n - 1) return nLayers + 1;
                    if (next >= 0 and next < n and !visited[next]) {
                        todo.push(next);
                        visited[next] = true;
                    }
                }
                numIdxes[arr[curr]].clear();
            }
            ++nLayers;
        }
        return -1;
    }
};
