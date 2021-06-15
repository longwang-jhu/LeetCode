// https://leetcode.com/problems/online-stock-span/

// Write a class StockSpanner which collects daily price quotes for some stock, and
// returns the span of that stock's price for the current day.

// The span of the stock's price today is defined as the maximum number of
// consecutive days (starting from today and going backwards) for which the price
// of the stock was less than or equal to today's price.

// For example, if the price of a stock over the next 7 days were [100, 80, 60, 70,
// 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

////////////////////////////////////////////////////////////////////////////////

// find prev greater num -> monoqueue
// use pair(price, span), instead of pair(price, idx)
class StockSpanner {
public:
    stack<pair<int, int>> toRight; // ele = (price, span)
    StockSpanner() {}
    int next(int price) {
        int span = 1;
        // pop if not greater
        while (!toRight.empty() and toRight.top().first <= price) {
            span += toRight.top().second; // accumulate spans
            toRight.pop();
        }
        toRight.push(make_pair(price, span));
        return span;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */
