// https://leetcode.com/problems/top-k-frequent-elements/

// Given an integer array nums and an integer k, return the k most frequent
// elements. You may return the answer in any order.

////////////////////////////////////////////////////////////////////////////////

// bucket sort, buckets[count] = nums of with that many counts
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // counts[num] = count of num
        unordered_map<int, int> counts;
        int maxCount;
        for (auto& num : nums) maxCount = max(maxCount, ++counts[num]);
        // buckets[count] = nums of with that many counts
        vector<vector<int>> buckets(maxCount + 1);
        for (auto& [num, count] : counts) buckets[count].push_back(num);
        
        vector<int> ans;
        for (int i = maxCount; i >= 0; --i) {
            for (auto& num : buckets[i]) {
                ans.push_back(num);
                if (ans.size() == k) return ans;
            }
        }
        return {};
    }
};
