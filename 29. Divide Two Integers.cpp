// https://leetcode.com/problems/divide-two-integers/

// Given two integers dividend and divisor, divide two integers without using
// multiplication, division, and mod operator.

// Return the quotient after dividing dividend by divisor.

// The integer division should truncate toward zero, which means losing its
// fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

// Note: Assume we are dealing with an environment that could only store integers
// within the 32-bit signed integer range: [−231, 231 − 1]. For this problem,
// assume that your function returns 231 − 1 when the division result overflows.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == 0) return 0;
        if (divisor == 1) return dividend;
        if (divisor == -1) return (dividend == INT_MIN) ? INT_MAX : -dividend;
        if (divisor == INT_MIN) return (dividend == INT_MIN) ? 1 : 0;
        
        int ans = 0;
        int sign = ((dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)) ? 1 : -1;
        
        // abs(INT_MIN) will overflow
        if (dividend == INT_MIN) {
            dividend += abs(divisor);
            ++ans;
        }
        
        int a = abs(dividend), b = abs(divisor);
        ans += dividePositive(a, b);
        return sign * ans;
    }
    
    int dividePositive(int a, int b) {
        if (a < b) return 0;
        // find count such that b * count <= a
        int bMulti = b, count = 1;
        while (bMulti <= a - bMulti) { // bMulti + bMulti <= a will overflow
            count *= 2;
            bMulti *= 2;
        }
        return count + dividePositive(a - bMulti, b);
    }
};
