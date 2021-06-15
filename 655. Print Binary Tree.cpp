// https://leetcode.com/problems/print-binary-tree/

// Given the root of a binary tree, construct a 0-indexed m x n string matrix res
// that represents a formatted layout of the tree. The formatted layout matrix
// should be constructed using the following rules:

// Return the constructed matrix res.

////////////////////////////////////////////////////////////////////////////////

// get height and width to initialize ans
// dfs to update ans
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
    vector<vector<string>> printTree(TreeNode* root) {
        int height = getHeight(root);
        int width = getWidth(root);
        ans = vector<vector<string>>(height, vector<string>(width, ""));
        dfs(root, 0, 0, width - 1);
        return ans;
    }
private:
    vector<vector<string>> ans;
    int getHeight(TreeNode* root) {
        if (root == nullptr) return 0;
        int leftHeight = getHeight(root->left);
        int rightHeight = getHeight(root->right);
        return 1 + max(leftHeight, rightHeight);
    }
    
    int getWidth(TreeNode* root) {
        if (root == nullptr) return 0;
        int leftWidth = getWidth(root->left);
        int rightWidth = getWidth(root->right);
        return max(leftWidth, rightWidth) * 2 + 1;
    }
    
    void dfs(TreeNode* root, int level, int left, int right) {
        if (root == nullptr) return;
        int mid = left + (right - left) / 2;
        ans[level][mid] = to_string(root->val);
        dfs(root->left, level + 1, left, mid - 1);
        dfs(root->right, level + 1, mid + 1, right);
    }
};
