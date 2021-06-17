// https://leetcode.com/problems/sqrtx/

// Given a non-negative integer x, compute and return the square root of x.

// Since the return type is an integer, the decimal digits are truncated, and only
// the integer part of the result is returned.

// Note: You are not allowed to use any built-in exponent function or operator,
// such as pow(x, 0.5) or x ** 0.5.

////////////////////////////////////////////////////////////////////////////////

// binary search
class Solution {
public:
    int mySqrt(int x) {
        if (x <= 1) return x;
        int l = 1, r = x / 2;
        while (l + 1 < r) {
            int m = l + (r - l) / 2;
            if (m == x / m) return m;
            if (m < x / m) l = m;
            else r = m;
        }
        // l * l <= x <= r * r
        return (r > x / r) ? l : r;
    }
};
