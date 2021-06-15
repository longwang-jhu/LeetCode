// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

// Given the root of a binary tree, return the zigzag level order traversal of its
// nodes' values. (i.e., from left to right, then right to left for the next level
// and alternate between).

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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (root == nullptr) return {};
        
        vector<vector<int>> ans;
        vector<int> thisLayer;
        bool toRight = true;
        deque<TreeNode*> dq; dq.push_back(root);
        while (!dq.empty()) {
            int nThisLayer = dq.size();
            while (nThisLayer--) {
                if (toRight) {
                    TreeNode* node = dq.front(); dq.pop_front();
                    thisLayer.push_back(node->val);
                    if (node->left != nullptr) dq.push_back(node->left);
                    if (node->right != nullptr) dq.push_back(node->right);
                } else {
                    TreeNode* node = dq.back(); dq.pop_back();
                    thisLayer.push_back(node->val);
                    if (node->right != nullptr) dq.push_front(node->right);
                    if (node->left != nullptr) dq.push_front(node->left);
                }
            }
            ans.push_back(thisLayer);
            thisLayer.clear();
            toRight = !toRight;
        }
        return ans;
    }
};
