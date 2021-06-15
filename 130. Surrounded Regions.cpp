// https://leetcode.com/problems/surrounded-regions/

// Given an m x n matrix board containing 'X' and 'O', capture all regions
// surrounded by 'X'.

// A region is captured by flipping all 'O's into 'X's in that surrounded region.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<pair<int, int>> dirs = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    void solve(vector<vector<char>>& board) {
        int m = board.size(), n = board[0].size();
        // dfs from edges, mark 'O' to 'S'
        for (int i = 0; i < m; ++i) {
            if (board[i][0] == 'O') dfs(board, i, 0);
            if (board[i][n - 1] == 'O') dfs(board, i, n - 1);
        }
        for (int j = 0; j < n; ++j) {
            if (board[0][j] == 'O') dfs(board, 0, j);
            if (board[m - 1][j] == 'O') dfs(board, m - 1, j);
        }
        // mark 'O' to 'X' and 'S' to 'O';
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] == 'O') board[i][j] = 'X';
                if (board[i][j] == 'S') board[i][j] = 'O';
            }
        }
        return;
    }
    
    void dfs(vector<vector<char>>& board, int i, int j) {
        board[i][j] = 'S';
        for (auto& [iIncr, jIncr] : dirs) {
            int iNext = i + iIncr;
            int jNext = j + jIncr;
            if (iNext >= 0 and iNext < board.size() and jNext >= 0 and jNext < board[0].size()
                and board[iNext][jNext] == 'O') dfs(board, iNext, jNext);
        }
        return;
    }
};
