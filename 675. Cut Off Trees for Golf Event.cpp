// https://leetcode.com/problems/cut-off-trees-for-golf-event/

// You are asked to cut off all the trees in a forest for a golf event. The forest
// is represented as an m x n matrix. In this matrix:

// In one step, you can walk in any of the four directions: north, east, south, and
// west. If you are standing in a cell with a tree, you can choose whether to cut
// it off.

// You must cut off the trees in order from shortest to tallest. When you cut off a
// tree, the value at its cell becomes 1 (an empty cell).

// Starting from the point (0, 0), return the minimum steps you need to walk to cut
// off all the trees. If you cannot cut off all the trees, return -1.

// You are guaranteed that no two trees have the same height, and there is at least
// one tree needs to be cut off.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<pair<int, int>> dirs = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    int cutOffTree(vector<vector<int>>& forest) {
        int m = forest.size(), n = forest[0].size();
        vector<tuple<int, int, int>> trees; // trees = {{height, i, j}}
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (forest[i][j] > 1) trees.push_back(make_tuple(forest[i][j], i, j));
            }
        }
        sort(trees.begin(), trees.end());
        
        int ans = 0, iS = 0, jS = 0;
        for (auto& [height, iT, jT] : trees) {
            int step = bfs(forest, iS, jS, iT, jT); // steps from (iS, jS) to (iT, jT)
            if (step == -1) return -1;
            ans += step; iS = iT; jS = jT;
        }
        return ans;
    }

    int bfs(vector<vector<int>>& forest, int iS, int jS, int iT, int jT) {
        if (iS == iT and jS == jT) return 0;
        int m = forest.size(), n = forest[0].size();
        queue<pair<int, int>> todo; todo.push({iS, jS}); 
        vector<vector<bool>> visited(m, vector<bool>(n, false)); visited[iS][jS] = true;
        
        int step = 0;
        while (!todo.empty()) {
            int nThisLayer = todo.size();
            while (nThisLayer--) {
                auto [i, j] = todo.front(); todo.pop();
                for (auto& [iIncr, jIncr] : dirs) {
                    int iNext = i + iIncr, jNext = j + jIncr;
                    if (iNext == iT and jNext == jT) return ++step;
                    if (iNext >= 0 and iNext < m and jNext >= 0 and jNext < n
                        and !visited[iNext][jNext] and forest[iNext][jNext] != 0) {
                        todo.push(make_pair(iNext, jNext));
                        visited[iNext][jNext] = true;
                    }
                }
            }
            ++step;
        }
        return -1;
    }
};
