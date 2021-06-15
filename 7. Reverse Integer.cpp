// https://leetcode.com/problems/reverse-integer/

// Given a signed 32-bit integer x, return x with its digits reversed. If reversing
// x causes the value to go outside the signed 32-bit integer range [-231, 231 -
// 1], then return 0.

// Assume the environment does not allow you to store 64-bit integers (signed or
// unsigned).

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    int reverse(int x) {
        int ans = 0;
        while (x != 0) {
            int lastDig = x % 10;
            // check overflow
            if (ans > INT_MAX / 10 or (ans == INT_MAX / 10 and lastDig > 7)) return 0;
            if (ans < INT_MIN / 10 or (ans == INT_MIN / 10 and lastDig < -8)) return 0;
            ans = ans * 10 + lastDig;
            x /= 10;
        }
        return ans;        
    }
};
