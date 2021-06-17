// https://leetcode.com/problems/surrounded-regions/

// Given an m x n matrix board containing 'X' and 'O', capture all regions
// surrounded by 'X'.

// A region is captured by flipping all 'O's into 'X's in that surrounded region.

////////////////////////////////////////////////////////////////////////////////

// dfs to grow from edges, filp the rest
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        m = board.size(); n = board[0].size();
        // dfs from edges, mark 'O' to 'S'
        for (int i = 0; i < m; ++i) {
            if (board[i][0] == 'O') dfs(i, 0, board);
            if (board[i][n - 1] == 'O') dfs(i, n - 1, board);
        }
        for (int j = 0; j < n; ++j) {
            if (board[0][j] == 'O') dfs(0, j, board);
            if (board[m - 1][j] == 'O') dfs(m - 1, j, board);
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
private:
    int m, n;
    vector<pair<int, int>> dirs = {{1,0}, {0,1}, {-1,0}, {0,-1}};
    void dfs(int i, int j, vector<vector<char>>& board) {
        board[i][j] = 'S';
        for (const auto& [iIncr, jIncr] : dirs) {
            int iNext = i + iIncr, jNext = j + jIncr;
            if (iNext >= 0 && iNext < m && jNext >= 0 && jNext < n
                && board[iNext][jNext] == 'O') {
                dfs(iNext, jNext, board);
            }
        }
        return;
    }
};
