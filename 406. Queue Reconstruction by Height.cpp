// https://leetcode.com/problems/queue-reconstruction-by-height/

// You are given an array of people, people, which are the attributes of some
// people in a queue (not necessarily in order). Each people[i] = [hi, ki]
// represents the ith person of height hi with exactly ki other people in front who
// have a height greater than or equal to hi.

// Reconstruct and return the queue that is represented by the input array people.
// The returned queue should be formatted as an array queue, where queue[j] = [hj,
// kj] is the attributes of the jth person in the queue (queue[0] is the person at
// the front of the queue).

////////////////////////////////////////////////////////////////////////////////

// sort, put highest people in front, insert to ans at idx k
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(),
             [](vector<int>& a, vector<int>& b) {
                 if (a[0] == b[0]) return a[1] < b[1];
                 return a[0] > b[0];
             });
        
        vector<vector<int>> ans;
        for (const auto& p : people) {
            ans.insert(ans.begin() + p[1], p);
        }
        return ans;
    }
};
