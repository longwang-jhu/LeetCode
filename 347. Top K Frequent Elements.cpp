// https://leetcode.com/problems/top-k-frequent-elements/

// Given an integer array nums and an integer k, return the k most frequent
// elements. You may return the answer in any order.

////////////////////////////////////////////////////////////////////////////////

// bucket sort
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // counts[num] = count of num
        unordered_map<int, int> counts;
        int maxCount;
        for (int &num : nums) maxCount = max(maxCount, ++counts[num]);
        
        // buckets[count] = nums of with that many counts
        vector<vector<int>> buckets(maxCount + 1);
        for (auto &[num, count] : counts) buckets[count].push_back(num);
        
        vector<int> ans;
        for (int i = maxCount; i >= 0 and ans.size() < k; --i) {
            for (int &num : buckets[i]) {
                ans.push_back(num);
                if (ans.size() == k) break;
            }
        }
        return ans;
    }
};
