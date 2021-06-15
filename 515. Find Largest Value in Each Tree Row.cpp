// https://leetcode.com/problems/find-largest-value-in-each-tree-row/

// Given the root of a binary tree, return an array of the largest value in each
// row of the tree (0-indexed).

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
    vector<int> largestValues(TreeNode* root) {
        if (root == nullptr) return {};
        vector<int> ans;
        queue<TreeNode*> todo; todo.push(root);
        while (!todo.empty()) {
            int nThisLayer = todo.size();
            int layerMax = INT_MIN;
            while (nThisLayer--) {
                TreeNode* curr = todo.front(); todo.pop();
                if (curr->left) todo.push(curr->left);
                if (curr->right) todo.push(curr->right);
                layerMax = max(layerMax, curr->val);
            }
            ans.push_back(layerMax);
        }
        return ans;
    }
};
