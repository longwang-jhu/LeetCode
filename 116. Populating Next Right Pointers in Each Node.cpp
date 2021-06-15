// https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

// You are given a perfect binary tree where all leaves are on the same level, and
// every parent has two children. The binary tree has the following definition:

// Populate each next pointer to point to its next right node. If there is no next
// right node, the next pointer should be set to NULL.

// Initially, all next pointers are set to NULL.

////////////////////////////////////////////////////////////////////////////////

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        return connectO1(root);
        if (root == nullptr) return {};
        
        queue<Node*> q; q.push(root);
        while (!q.empty()) {
            int nThisLayer = q.size();
            Node* prevNode = nullptr;
            for (int i = 0; i < nThisLayer; ++i){
                Node* node = q.front(); q.pop();
                if (i > 0) prevNode->next = node;
                prevNode = node;
                if (node->left != nullptr) q.push(node->left);
                if (node->right != nullptr) q.push(node->right);
            }
        }
        return root;
    }
    
    Node* connectO1(Node* root) { // O(1) space
        if (root == nullptr) return {};
        Node* curr = root;
        while (curr != nullptr and curr->left != nullptr) {
            Node* next = curr->left;
            while (curr != nullptr) { // loop over this layer
                curr->left->next = curr->right;
                if (curr->next != nullptr) curr->right->next = curr->next->left;
                curr = curr->next;
            }
            curr = next;
        }
        return root;
    }
};
