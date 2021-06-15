// https://leetcode.com/problems/palindrome-number/

// Given an integer x, return true if x is palindrome integer.

// An integer is a palindrome when it reads the same backward as forward. For
// example, 121 is palindrome while 123 is not.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        if (x == 0) return true;
        if (x % 10 == 0) return false;
        
        int xRev = 0;
        while (x > xRev) {
            int lastDigit = x % 10;
            xRev = xRev * 10 + lastDigit;
            x /= 10;
        }
        return x == xRev or x == xRev / 10;
    }
};
