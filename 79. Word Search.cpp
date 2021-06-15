// https://leetcode.com/problems/word-search/

// Given an m x n grid of characters board and a string word, return true if word
// exists in the grid.

// The word can be constructed from letters of sequentially adjacent cells, where
// adjacent cells are horizontally or vertically neighboring. The same letter cell
// may not be used more than once.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<vector<int>> dirs = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size(), n = board[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        for (int i = 0; i < m; ++i){
            for (int j = 0; j < n; ++j) {
                if (dfs(board, word, visited, i, j, 0)) return true;
            }
        }
        return false;
    }
    
    bool dfs(const vector<vector<char>> &board, const string word,
             vector<vector<bool>> &visited, int i, int j, int pos) {
        if (board[i][j] != word[pos]) return false;
        if (pos == word.size() - 1) return true;
                
        visited[i][j] = true;        
        bool found = false;
        for (int dirIdx = 0; dirIdx < 4; ++dirIdx) {
            int iNext = i + dirs[dirIdx][0];
            int jNext = j + dirs[dirIdx][1];
            
            if (iNext >= 0 and iNext < board.size()
                and jNext >= 0 and jNext < board[0].size()
                and !visited[iNext][jNext]) {
                found = found or dfs(board, word, visited, iNext, jNext, pos + 1);
            }
        }
        visited[i][j] = false;
        return found;
    }
};
