// https://leetcode.com/problems/find-bottom-left-tree-value/

// Given the root of a binary tree, return the leftmost value in the last row of
// the tree.

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
    int findBottomLeftValue(TreeNode* root) {
        int ans;
        queue<TreeNode*> todo; todo.push(root);
        while (!todo.empty()) {
            int nThisLayer = todo.size();
            for (int i = 0; i < nThisLayer; ++i) {
                TreeNode* curr = todo.front(); todo.pop();
                if (curr->left != nullptr) todo.push(curr->left);
                if (curr->right != nullptr) todo.push(curr->right);
                if (i == 0) ans = curr->val; // store the left most val
            }
        }
        return ans;
    }
};
