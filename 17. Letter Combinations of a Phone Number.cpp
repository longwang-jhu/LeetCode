// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

// Given a string containing digits from 2-9 inclusive, return all possible letter
// combinations that the number could represent. Return the answer in any order.

// A mapping of digit to letters (just like on the telephone buttons) is given
// below. Note that 1 does not map to any letters.



////////////////////////////////////////////////////////////////////////////////

// dfs
class Solution {
public:
    vector<string> ans;
    string holder;
    unordered_map<char, string> hashMap;
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        hashMap = {{'2', "abc"}, {'3', "def"}, {'4', "ghi"},
                   {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"},
                   {'8', "tuv"}, {'9', "wxyz"}};
        dfs(digits, 0);
        return ans;
    }
    
    void dfs(string digits, int pos) {
        if (holder.size() == digits.size()) {
            ans.push_back(holder); return;
        }
        for (char c : hashMap[digits[pos]]) {
            holder.push_back(c);
            dfs(digits, pos + 1);
            holder.pop_back();
        }
        return;
    }
};
