// https://leetcode.com/problems/sum-of-square-numbers/

// Given a non-negative integer c, decide whether there're two integers a and b
// such that a2 + b2 = c.

////////////////////////////////////////////////////////////////////////////////

// two sum
class Solution {
public:
    bool judgeSquareSum(int c) {
        int left = 0, right = sqrt(c);
        while (left <= right) {
            long int total = (long int) left * left + right * right;
            if (total == c) return true;
            if (total < c) ++left;
            else --right;
        }
        return false;
    }
};
