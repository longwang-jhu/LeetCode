// https://leetcode.com/problems/remove-k-digits/

// Given string num representing a non-negative integer num, and an integer k,
// return the smallest possible integer after removing k digits from num.

////////////////////////////////////////////////////////////////////////////////

// remove prevDigit if it is greater
class Solution {
public:
    string removeKdigits(string num, int k) {
        if (k >= num.size()) return "0";
        int n = num.size();
        deque<int> toRight;
        for (int i = 0; i < n; ++i) {
            while (k > 0 and !toRight.empty() and toRight.back() > num[i]) {
                toRight.pop_back(); --k;
            }
            toRight.push_back(num[i]);
        }
        while (k--) toRight.pop_back();
        while (!toRight.empty() and toRight.front() == '0') toRight.pop_front();
        
        string ans;
        while (!toRight.empty()) {
            ans += toRight.front(); toRight.pop_front();
        }
        return ans.empty() ? "0" : ans;
    }
};
