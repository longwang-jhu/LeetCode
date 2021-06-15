// https://leetcode.com/problems/swap-nodes-in-pairs/

// Given a linked list, swap every two adjacent nodes and return its head. You must
// solve the problem without modifying the values in the list's nodes (i.e., only
// nodes themselves may be changed.)

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
    ListNode* swapPairs(ListNode* head) {
        if (!head or !head->next) return head;
        ListNode *dummy = new ListNode();
        dummy->next = head;
        ListNode *ptrPrev = dummy, *ptrCurr = head;
        // swap ptrCurr and ptrCurr->next
        while (ptrCurr and ptrCurr->next) {
            // ptrPrev -> ptrCurr -> ptrNext ->
            ListNode *ptrNext = ptrCurr->next;
            ptrPrev->next = ptrNext;
            
            // ptrPrev -> ptrNext -> ptrCurr ->
            ptrCurr->next = ptrNext->next;
            ptrNext->next = ptrCurr; 
            
            // move on
            ptrPrev = ptrCurr;
            ptrCurr = ptrCurr->next;
        }
        return dummy->next;
    }
};
