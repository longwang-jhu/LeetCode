// https://leetcode.com/problems/merge-k-sorted-lists/

// You are given an array of k linked-lists lists, each linked-list is sorted in
// ascending order.

// Merge all the linked-lists into one sorted linked-list and return it.

////////////////////////////////////////////////////////////////////////////////

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode *dummy = new ListNode(), *curr = dummy;
        // put vals into minpq
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minpq;
        for (size_t i = 0, n = lists.size(); i < n; ++i) {
            if (lists[i] != nullptr) minpq.push(make_pair(lists[i]->val, i));
        }
        while (!minpq.empty()) {
            auto [val, idx] = minpq.top(); minpq.pop();
            curr->next = new ListNode(val); curr = curr->next;
            // move ListNode and push to minpq
            if (lists[idx]->next != nullptr) {
                lists[idx] = lists[idx]->next;
                minpq.push(make_pair(lists[idx]->val, idx));
            }
        }
        return dummy->next;
    }
};
