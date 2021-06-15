// https://leetcode.com/problems/minimum-depth-of-binary-tree/

// Given a binary tree, find its minimum depth.

// The minimum depth is the number of nodes along the shortest path from the root
// node down to the nearest leaf node.

// Note: A leaf is a node with no children.

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
    int minDepth(TreeNode* root) {
        if (root == nullptr) return 0;
        
        int depth = 0;
        queue<TreeNode*> q; q.push(root);
        while (!q.empty()) {
            int nThisLayer = q.size();
            while (nThisLayer--) {
                TreeNode* node = q.front(); q.pop();
                if (node->left == nullptr and node->right == nullptr) return depth + 1;
                if (node->left != nullptr) q.push(node->left);
                if (node->right != nullptr) q.push(node->right);
            }
            ++depth;
        }
        return depth;
    }
};
