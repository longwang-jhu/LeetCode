// https://leetcode.com/problems/can-place-flowers/

// You have a long flowerbed in which some of the plots are planted, and some are
// not. However, flowers cannot be planted in adjacent plots.

// Given an integer array flowerbed containing 0's and 1's, where 0 means empty and
// 1 means not empty, and an integer n, return if n new flowers can be planted in
// the flowerbed without violating the no-adjacent-flowers rule.

////////////////////////////////////////////////////////////////////////////////

// greedy
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        if (n == 0) return true;
        int planted = 0, i = 0;
        while (i < flowerbed.size()) {
            if (flowerbed[i] == 0
                && (i == 0 || flowerbed[i - 1] == 0)
                && (i == flowerbed.size() - 1 || flowerbed[i + 1] == 0)) {
                if (++planted >= n) return true;
                flowerbed[i] = 1;
            }
            ++i;
        }
        return false;
    }
};
