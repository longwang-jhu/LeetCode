// https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

// Given the root of a binary tree, return the bottom-up level order traversal of
// its nodes' values. (i.e., from left to right, level by level from leaf to root).

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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        if (root == nullptr) return {};
        
        vector<vector<int>> ans;
        vector<int> thisLayer;
        queue<TreeNode*> q; q.push(root);
        while (!q.empty()) {
            int nThisLayer = q.size();
            while (nThisLayer--) {
                TreeNode* node = q.front(); q.pop();
                thisLayer.push_back(node->val);
                if (node->left != nullptr) q.push(node->left);
                if (node->right != nullptr) q.push(node->right);
            }
            ans.push_back(thisLayer);
            thisLayer.clear();
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
