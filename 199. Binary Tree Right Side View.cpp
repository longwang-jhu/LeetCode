// https://leetcode.com/problems/binary-tree-right-side-view/

// Given the root of a binary tree, imagine yourself standing on the right side of
// it, return the values of the nodes you can see ordered from top to bottom.

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
    vector<int> rightSideView(TreeNode* root) {
        if (root == nullptr) return {};
        vector<int> ans;
        queue<TreeNode*> todo; todo.push(root);
        while (!todo.empty()) {
            int nThisLayer = todo.size();
            while (nThisLayer--) {
                TreeNode* curr = todo.front(); todo.pop();
                if (nThisLayer == 0) ans.push_back(curr->val);
                if (curr->left) todo.push(curr->left);
                if (curr->right) todo.push(curr->right);
            }
        }
        return ans;
    }
};
