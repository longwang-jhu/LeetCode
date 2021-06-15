// https://leetcode.com/problems/sliding-puzzle/

// On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and
// an empty square represented by 0.

// A move consists of choosing 0 and a 4-directionally adjacent number and swapping
// it.

// The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

// Given a puzzle board, return the least number of moves required so that the
// state of the board is solved. If it is impossible for the state of the board to
// be solved, return -1.

// Examples:

// Note:

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<pair<int,int>> dirs = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    int slidingPuzzle(vector<vector<int>>& board) {
        int m = board.size(), n = board[0].size();
        string target = "123450";
        stringstream ss;
        for (int i : {0, 1}) copy(board[i].begin(), board[i].end(), ostream_iterator<int>(ss));
        string source = ss.str();
        if (source == target) return 0;
        
        // bfs
        queue<string> q; q.push(source);
        unordered_set<string> visited; visited.insert(source);
        int ans = 0;
        while(!q.empty()) {
            int nThisLayer = q.size();
            while (nThisLayer--) {
                string s = q.front(); q.pop();
                // generate neighbors
                int i = s.find('0'), x = i / n, y = i % n;
                for (auto [xDelta, yDelta] : dirs) {
                    int xNext = x + xDelta;
                    int yNext = y + yDelta;
                    if (xNext >= 0 and xNext < m and yNext >= 0 and yNext < n) {
                        int iNext = xNext * n + yNext;
                        string sNext = s; swap(sNext[i], sNext[iNext]);
                        if (sNext == target) return ++ans;
                        if (visited.find(sNext) == visited.end()) {
                            q.push(sNext);
                            visited.insert(sNext);
                        }
                    }
                }
            }
            ++ans;
        }
        return -1;
    }
};
