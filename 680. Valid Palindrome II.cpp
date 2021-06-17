// https://leetcode.com/problems/valid-palindrome-ii/

// Given a string s, return true if the s can be palindrome after deleting at most
// one character from it.

////////////////////////////////////////////////////////////////////////////////

// l and r ptrs
class Solution {
public:
    bool validPalindrome(string s) {
        int l = 0, r = s.size() - 1;
        while (l < r) {
            if (s[l] == s[r]) { ++l; --r; }
            else {
                return isPalindrome(s, l + 1, r) || isPalindrome(s, l, r - 1);
            }
        }
        return true;
    }
private:
    bool isPalindrome(string& s, int l, int r) {
        while (l < r) {
            if (s[l] == s[r]) { ++l; --r; }
            else return false;
        }
        return true;
    }
};
