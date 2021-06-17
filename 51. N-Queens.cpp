// https://leetcode.com/problems/n-queens/

// The n-queens puzzle is the problem of placing n queens on an n x n chessboard
// such that no two queens attack each other.

// Given an integer n, return all distinct solutions to the n-queens puzzle. You
// may return the answer in any order.

// Each solution contains a distinct board configuration of the n-queens'
// placement, where 'Q' and '.' both indicate a queen and an empty space,
// respectively.

////////////////////////////////////////////////////////////////////////////////

// dfs, place by row
// diag: (2n+1) lines, i = row - col + n - 1, counting from top-right
// antiDiag: (2n+1) lines, i = row + col, counting from top-left
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        colUsed = vector<bool>(n, false);
        diagUsed = vector<bool>(2 * n + 1, false);
        antiDiagUsed = vector<bool>(2 * n + 1, false);
        dfs(0, n);
        return ans;
    }
private:
    vector<bool> colUsed, diagUsed, antiDiagUsed;
    vector<string> holder;
    vector<vector<string>> ans;
    void dfs(int row, const int& n) {
        if (row == n) {
            ans.push_back(holder); return;
        }
        for (int col = 0; col < n; ++col){ // children
            if (!colUsed[col] && !diagUsed[row - col + n - 1]
                && !antiDiagUsed[row + col]) {
                // place queen
                string holderRow(n, '.');
                holderRow[col] = 'Q';
                holder.push_back(holderRow);
                colUsed[col] = true;
                diagUsed[row - col + n - 1] = true;
                antiDiagUsed[row + col] = true;
                // go to child
                dfs(row + 1, n);
                // remove queen
                holder.pop_back();
                colUsed[col] = false;
                diagUsed[row - col + n - 1] = false;
                antiDiagUsed[row + col] = false;
            }
        }
    }
};
