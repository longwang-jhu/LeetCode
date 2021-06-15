// https://leetcode.com/problems/can-place-flowers/

// You have a long flowerbed in which some of the plots are planted, and some are
// not. However, flowers cannot be planted in adjacent plots.

// Given an integer array flowerbed containing 0's and 1's, where 0 means empty and
// 1 means not empty, and an integer n, return if n new flowers can be planted in
// the flowerbed without violating the no-adjacent-flowers rule.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        if (n == 0) return true;
        
        int planted = 0, i = 0;
        while (i < flowerbed.size()) {
            if (flowerbed[i] == 0
                and (i == 0 or flowerbed[i-1] == 0)
                and (i == flowerbed.size() - 1 or flowerbed[i+1] == 0)) {
                
                ++planted;
                flowerbed[i] = 1;
            }
            ++i;
        }
        return planted >= n;
    }
};
