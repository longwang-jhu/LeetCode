// https://leetcode.com/problems/linked-list-cycle-ii/

// Given a linked list, return the node where the cycle begins. If there is no
// cycle, return null.

// There is a cycle in a linked list if there is some node in the list that can be
// reached again by continuously following the next pointer. Internally, pos is
// used to denote the index of the node that tail's next pointer is connected to.
// Note that pos is not passed as a parameter.

// Notice that you should not modify the linked list.

////////////////////////////////////////////////////////////////////////////////

// slow and fast ptrs
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (!head or !head->next) return nullptr;
                
        ListNode *slow = head, *fast = head;
        bool isCycle = false;
        while (fast->next and fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
            
            if (slow == fast) {
                isCycle = true;
                break;
            }
        }
        
        if (!isCycle) return nullptr;
        slow = head;
        while (slow != fast) {
            slow = slow->next;
            fast = fast->next;
        }
        return slow;
    }
};
