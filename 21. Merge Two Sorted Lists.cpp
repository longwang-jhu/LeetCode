// https://leetcode.com/problems/merge-two-sorted-lists/

// Merge two sorted linked lists and return it as a sorted list. The list should be
// made by splicing together the nodes of the first two lists.

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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *dummy = new ListNode(), *curr = dummy;
        while (l1 != nullptr and l2 != nullptr) {
            if (l1->val < l2->val) {
                curr->next = new ListNode(l1->val);
                curr = curr->next; l1 = l1->next;
            } else {
                curr->next = new ListNode(l2->val);
                curr = curr->next; l2 = l2->next;
            }
        }
        if (l1 != nullptr) curr->next = l1;
        if (l2 != nullptr) curr->next = l2;
        return dummy->next;
    }
};
