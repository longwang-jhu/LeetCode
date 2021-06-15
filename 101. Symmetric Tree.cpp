// https://leetcode.com/problems/symmetric-tree/

// Given the root of a binary tree, check whether it is a mirror of itself (i.e.,
// symmetric around its center).

////////////////////////////////////////////////////////////////////////////////

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        return isMirror(root, root);
    }
    
    bool isMirror(TreeNode* node1, TreeNode* node2) {
        if (!node1 and !node2) return true;
        if (!node1 or !node2) return false;
        if (node1->val != node2->val) return false;
        return isMirror(node1->left, node2->right) and isMirror(node1->right, node2->left);
    }
};
