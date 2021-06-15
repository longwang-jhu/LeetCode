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
// diag: (2n+1) lines, row - col + n - 1 = i, counting from top-right
// antiDiag: (2n+1) lines, row + col = i, counting from top-left

class Solution {
public:
    vector<vector<string>> ans;
    vector<string> holder;
    
    vector<vector<string>> solveNQueens(int n) {
        vector<bool> colUsed(n, false);
        vector<bool> diagUsed(2 * n + 1, false);
        vector<bool> antiDiagUsed(2 * n + 1, false);
        
        dfs(n, colUsed, diagUsed, antiDiagUsed, 0);
        return ans;
    }
    
    void dfs(const int n, vector<bool> &colUsed, vector<bool> &diagUsed,
             vector<bool> &antiDiagUsed, int row) {
        if (row == n) {
            ans.push_back(holder);
            return;
        }
        
        // generate children
        for (int col = 0; col < n; ++col){
            if (!colUsed[col] and !diagUsed[row - col + n - 1]
                and !antiDiagUsed[row + col]) {
                // place queen
                string holderRow(n, '.');
                holderRow[col] = 'Q';
                holder.push_back(holderRow);

                // update free position
                colUsed[col] = true;
                diagUsed[row - col + n - 1] = true;
                antiDiagUsed[row + col] = true;
                
                // go to child
                dfs(n, colUsed, diagUsed, antiDiagUsed, row + 1);
                
                // remore queen
                holder.pop_back();
                colUsed[col] = false;
                diagUsed[row - col + n - 1] = false;
                antiDiagUsed[row + col] = false;
            }
        }
    }
};
