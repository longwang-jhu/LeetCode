// https://leetcode.com/problems/integer-to-roman/

// Roman numerals are represented by seven different symbols: I, V, X, L, C, D and
// M.

// For example, 2 is written as II in Roman numeral, just two one's added together.
// 12 is written as XII, which is simply X + II. The number 27 is written as XXVII,
// which is XX + V + II.

// Roman numerals are usually written largest to smallest from left to right.
// However, the numeral for four is not IIII. Instead, the number four is written
// as IV. Because the one is before the five we subtract it making four. The same
// principle applies to the number nine, which is written as IX. There are six
// instances where subtraction is used:

// Given an integer, convert it to a roman numeral.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    string intToRoman(int num) {
        vector<int> values = {1000, 900, 500, 400, 100, 
                              90, 50, 40, 10, 9, 5, 4, 1};
        vector<string> symbols = {"M", "CM", "D", "CD", "C", "XC", 
                                  "L", "XL", "X", "IX", "V", "IV", "I"};
        string ans;
        for (int i = 0; i < values.size(); ++i) {
            while (num >= values[i]) {
                num -= values[i];
                ans += symbols[i];
            }
        }
        return ans;
    }
};
