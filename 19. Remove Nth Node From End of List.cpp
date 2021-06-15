// https://leetcode.com/problems/remove-nth-node-from-end-of-list/

// Given the head of a linked list, remove the nth node from the end of the list
// and return its head.

////////////////////////////////////////////////////////////////////////////////

// use slow and fast ptrs
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *dummy = new ListNode();
        dummy->next = head;
        ListNode *slow = dummy, *fast = dummy;
        
        while (n-- > 0) fast = fast->next; // move fast n times;
        while (fast->next) { // move slow and fast until fast is at end
            slow = slow->next;
            fast = fast->next;
        }
        slow->next = slow->next->next; // skip the desire node
        return dummy->next;
    }
};
