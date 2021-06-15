// https://leetcode.com/problems/perfect-number/

// A perfect number is a positive integer that is equal to the sum of its positive
// divisors, excluding the number itself. A divisor of an integer x is an integer
// that can divide x evenly.

// Given an integer n, return true if n is a perfect number, otherwise return
// false.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num <= 0) return false;
        int total = 0;
        for (int i = 1; i * i <= num; ++i) {
            if (num % i == 0) {
                total += i;
                if (i * i != num) total += num / i;
            }
        }
        return total == num + num;
    }
};
