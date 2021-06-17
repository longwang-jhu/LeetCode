// https://leetcode.com/problems/sudoku-solver/

// Write a program to solve a Sudoku puzzle by filling the empty cells.

// A sudoku solution must satisfy all of the following rules:

// The '.' character indicates empty cells.

////////////////////////////////////////////////////////////////////////////////

// dfs
class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        dfs(0, 0, board);
        return;
    }
private:
    bool dfs(int i, int j, vector<vector<char>>& board) {
        if (i == 9) return true;
        if (j == 9) return dfs(i + 1, 0, board);
        if (board[i][j] != '.') return dfs(i, j + 1, board);
        for (int val = 1; val <= 9; ++val) {
            if (!isValid(i, j, val, board)) continue;
            board[i][j] = '0' + val;
            if (dfs(i, j + 1, board)) return true;
            board[i][j] = '.';
        }
        return false;
    }
    // check if can set board[i][j] = val
    bool isValid(int i, int j, int val, const vector<vector<char>> board) {
        for (int k = 0; k < 9; ++k) {
            if (board[i][k] == '0' + val
                || board[k][j] == '0' + val
                || board[i/3*3 + k/3][j/3*3 + k%3] == '0' + val) {
                return false;
            }
        }
        return true;
    }
};
