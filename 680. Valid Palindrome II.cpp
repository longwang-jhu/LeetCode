// https://leetcode.com/problems/valid-palindrome-ii/

// Given a string s, return true if the s can be palindrome after deleting at most
// one character from it.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    bool validPalindrome(string s) {
        int left = 0, right = s.size() - 1;
        while (left < right) {
            if (s[left] == s[right]) { ++left; --right; }
            else {
                return isPalindrome(s, left + 1, right) or isPalindrome(s, left, right - 1);
            }
        }
        return true;
    }
    
    bool isPalindrome(string& s, int left, int right) {
        while (left < right) {
            if (s[left] == s[right]) { ++left; --right; }
            else return false;
        }
        return true;
    }
};
