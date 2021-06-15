// https://leetcode.com/problems/reverse-nodes-in-k-group/

// Given a linked list, reverse the nodes of a linked list k at a time and return
// its modified list.

// k is a positive integer and is less than or equal to the length of the linked
// list. If the number of nodes is not a multiple of k then left-out nodes, in the
// end, should remain as it is.

// You may not alter the values in the list's nodes, only nodes themselves may be
// changed.

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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* dummy = new ListNode(); dummy->next = head;
        ListNode* ptrCurr = dummy;
        ListNode* ptrHeadPrev = dummy;
        while (ptrCurr->next) {
            // move ptrCurr k times to thisTail
            for (int i = 0; i < k; ++i) {
                ptrCurr = ptrCurr->next;
                if (ptrCurr == nullptr) return dummy->next;
            }
            // ptrHeadPrev -> (ptrHead -> ... -> ptrTail) -> ptrTailNext
            ListNode* ptrHead = ptrHeadPrev->next;
            ListNode* ptrTail = ptrCurr;
            ListNode* ptrTailNext = ptrCurr->next;
            // ptrHeadPrev -> (ptrTail -> ... -> ptrHead) -> ptrTailNext            
            tie(ptrTail, ptrHead) = reverse(ptrHead, ptrTail);
            ptrHeadPrev->next = ptrTail;
            ptrHead->next = ptrTailNext;
            ptrHeadPrev = ptrHead;
            ptrCurr = ptrHead;
        }
        return dummy->next;
    }
    
    pair<ListNode*, ListNode*> reverse(ListNode* ptrHead, ListNode* ptrTail) {
        ListNode* ptrPrev = new ListNode();
        ListNode* ptrCurr = ptrHead;
        // reverse prev and curr
        while (ptrPrev != ptrTail) {
            ListNode *ptrNext = ptrCurr->next; // prev -> curr -> next
            ptrCurr->next = ptrPrev; // prev <- curr    next
            ptrPrev = ptrCurr;
            ptrCurr = ptrNext;
        }
        return make_pair(ptrTail, ptrHead);
    }
};
