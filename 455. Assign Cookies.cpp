// https://leetcode.com/problems/assign-cookies/

// Assume you are an awesome parent and want to give your children some cookies.
// But, you should give each child at most one cookie.

// Each child i has a greed factor g[i], which is the minimum size of a cookie that
// the child will be content with; and each cookie j has a size s[j]. If s[j] >=
// g[i], we can assign the cookie j to the child i, and the child i will be
// content. Your goal is to maximize the number of your content children and output
// the maximum number.

////////////////////////////////////////////////////////////////////////////////

// greedy -> sort, give smallest cookie to smallest child
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int child = 0, cookie = 0;
        while (child < g.size() && cookie < s.size()) {
            if (g[child] <= s[cookie]) ++child;
            ++cookie;
        }
        return child;
    }
};
