// https://leetcode.com/problems/minesweeper/

// Let's play the minesweeper game (Wikipedia, online game)!

// You are given an m x n char matrix board representing the game board where:

// You are also given an integer array click where click = [clickr, clickc]
// represents the next click position among all the unrevealed squares ('M' or
// 'E').

// Return the board after revealing this position according to the following rules:

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<pair<int, int>>dirs {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        int x = click[0], y = click[1];
        if (board[x][y] == 'M') board[x][y] = 'X';
        else dfs(board, x, y);
        return board;
    }
    
    bool inBoard(vector<vector<char>>& board, int x, int y) {
        return x >= 0 and x < board.size() and y >= 0 and y < board[0].size();
    }
        
    void dfs(vector<vector<char>>& board, int x, int y) {
        // check neigh mine
        int neighMine = 0;
        for (auto& [xIncr, yIncr] : dirs) {
            int xNext = x + xIncr;
            int yNext = y + yIncr;
            if (inBoard(board, xNext, yNext) and board[xNext][yNext] == 'M') ++neighMine;
        }
        if (neighMine > 0) board[x][y] = '0' + neighMine;
        else {
            board[x][y] = 'B';
            for (auto& [xIncr, yIncr] : dirs) {
                int xNext = x + xIncr;
                int yNext = y + yIncr;
                if (inBoard(board, xNext, yNext) and board[xNext][yNext] == 'E') {
                    dfs(board, xNext, yNext);
                }
            }
        }
        return;
    }
};
