// https://leetcode.com/problems/word-search/

// Given an m x n grid of characters board and a string word, return true if word
// exists in the grid.

// The word can be constructed from letters of sequentially adjacent cells, where
// adjacent cells are horizontally or vertically neighboring. The same letter cell
// may not be used more than once.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        m = board.size(); n = board[0].size();
        visited = vector<vector<bool>>(m, vector<bool>(n, false));
        for (int i = 0; i < m; ++i){
            for (int j = 0; j < n; ++j) {
                if (dfs(i, j, 0, board, word)) return true;
            }
        }
        return false;
    }
private:
    int m, n;
    vector<pair<int, int>> dirs = {{1,0}, {0,1}, {-1,0}, {0,-1}};
    vector<vector<bool>> visited;
    bool dfs(int i, int j, int pos,
             const vector<vector<char>>& board, const string& word) {
        if (board[i][j] != word[pos]) return false;
        if (pos == word.size() - 1) return true;
        visited[i][j] = true;
        for (const auto& [iIncr, jIncr] : dirs) {
            int iNext = i + iIncr, jNext = j + jIncr;
            if (iNext >= 0 && iNext < m && jNext >= 0 && jNext < n
                && !visited[iNext][jNext]) {
                if (dfs(iNext, jNext, pos + 1, board, word)) return true;
            }
        }
        visited[i][j] = false;
        return false;
    }
};
