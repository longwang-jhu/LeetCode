// https://leetcode.com/problems/jump-game-iii/

// Given an array of non-negative integers arr, you are initially positioned at
// start index of the array. When you are at index i, you can jump to i + arr[i] or
// i - arr[i], check if you can reach to any index with value 0.

// Notice that you can not jump outside of the array at any time.

////////////////////////////////////////////////////////////////////////////////

// bfs
class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        if (arr[start] == 0) return true;
        
        int n = arr.size();
        queue<int> todo; todo.push(start);
        vector<bool> visited(n, false); visited[start] = true;
        while (!todo.empty()) {
            int curr = todo.front(); todo.pop();
            for (int sign : {-1, 1}) {
                int next = curr + sign * arr[curr];
                if (next >= 0 and next < n) {
                    if (arr[next] == 0) return true;
                    if (!visited[next]) {
                        todo.push(next); visited[next] = true;
                    }
                }
            }
        }
        return false;
    }
};
