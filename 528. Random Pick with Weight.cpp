// https://leetcode.com/problems/random-pick-with-weight/

// You are given an array of positive integers w where w[i] describes the weight of
// ith index (0-indexed).

// We need to call the function pickIndex() which randomly returns an integer in
// the range [0, w.length - 1]. pickIndex() should return the integer proportional
// to its weight in the w array. For example, for w = [1, 3], the probability of
// picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of
// picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

// More formally, the probability of picking index i is w[i] / sum(w).

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<int> accu;
    std::default_random_engine gen;
    
    Solution(vector<int>& w) {
        for (int num : w) {
            if (accu.empty()) accu.push_back(num);
            else accu.push_back(accu.back() + num);
        }
    }
    
    int pickIndex() {
        std::uniform_int_distribution<int> distribution(0, accu.back() - 1);
        int u = distribution(gen);
        return upper_bound(accu.begin(), accu.end(), u) - accu.begin();
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
