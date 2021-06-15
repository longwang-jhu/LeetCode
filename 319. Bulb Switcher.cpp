// https://leetcode.com/problems/bulb-switcher/

// There are n bulbs that are initially off. You first turn on all the bulbs, then
// you turn off every second bulb.

// On the third round, you toggle every third bulb (turning on if it's off or
// turning off if it's on). For the ith round, you toggle every i bulb. For the nth
// round, you only toggle the last bulb.

// Return the number of bulbs that are on after n rounds.

////////////////////////////////////////////////////////////////////////////////

// bulb i is toggled (k = number of factors of i - 1) times
// Eg: factors of 4 are 1, 2, 4 -> 2 times
// Eg: factors of 6 are 1, 2, 3, 6 -> 3 times
// only perfect square is toggled even times => on at the end
// ans = number of perfect square <= n
// 1^2, 2^2, ..., ans^2 <= n

class Solution {
public:
    int bulbSwitch(int n) {
        return sqrt(n);
    }
};
