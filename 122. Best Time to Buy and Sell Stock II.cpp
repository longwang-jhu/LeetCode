// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

// You are given an array prices where prices[i] is the price of a given stock on
// the ith day.

// Find the maximum profit you can achieve. You may complete as many transactions
// as you like (i.e., buy one and sell one share of the stock multiple times).

// Note: You may not engage in multiple transactions simultaneously (i.e., you must
// sell the stock before you buy again).

////////////////////////////////////////////////////////////////////////////////

// greedy
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty() or prices.size() == 1) return 0;
        
        int profit = 0;
        for (int i = 1; i < prices.size(); ++i) {
            profit += max(0, prices[i] - prices[i-1]);
        }
        return profit;
    }
};
