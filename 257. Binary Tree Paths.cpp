// https://leetcode.com/problems/binary-tree-paths/

// Given the root of a binary tree, return all root-to-leaf paths in any order.

// A leaf is a node with no children.

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
    vector<string> binaryTreePaths(TreeNode* root) {
        holder.push_back(root->val);
        dfs(root);       
        return ans;
    }
private:
    vector<int> holder;
    vector<string> ans;
    void dfs(TreeNode* node) {
        if (!node->left and !node->right) {
            ans.push_back(toPath(holder)); return;
        }
        if (node->left) {
            holder.push_back(node->left->val);
            dfs(node->left);
            holder.pop_back();
        }
        if (node->right) {
            holder.push_back(node->right->val);
            dfs(node->right);
            holder.pop_back();
        }
        return;
    }
    string toPath(const vector<int>& holder) {
        string path = to_string(holder[0]);
        for (int i = 1; i < holder.size(); ++i) {
            path += "->" + to_string(holder[i]);
        }
        return path;
    }
};
