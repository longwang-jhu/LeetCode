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
        
        long int left = 1, right = x / 2, mid;
        while (left + 1 < right) {
            mid = left + (right - left) / 2;
            if (mid * mid == x) return mid;
            
            if (mid * mid < x) left = mid;
            else right = mid;
        }
        
        // left * left <= x <= right * right
        return (right * right <= x) ? right : left;
    }
};
