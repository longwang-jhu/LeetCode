// https://leetcode.com/problems/zigzag-conversion/

// The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
// rows like this: (you may want to display this pattern in a fixed font for better
// legibility)

// And then read line by line: "PAHNAPLSIIGYIR"

// Write the code that will take a string and make this conversion given a number
// of rows:

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) return s;
        
        vector<string> rows(numRows);
        int rowIdx = 0, rowIncr = 1;
        for (char &c : s) {
            rows[rowIdx] += c;
            rowIdx += rowIncr;
            if (rowIdx == numRows - 1 or rowIdx == 0) rowIncr *= -1; // reach the edges
        }
        string ans;
        for (string &row : rows)  ans += row;
        return ans;
    }
};
