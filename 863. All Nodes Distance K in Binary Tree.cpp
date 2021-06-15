// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

// We are given a binary tree (with root node root), a target node, and an integer
// value k.

// Return a list of the values of all nodes that have a distance k from the target
// node.  The answer can be returned in any order.

////////////////////////////////////////////////////////////////////////////////

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    // graph[node value] = set of neighbor node values
    unordered_map<int, unordered_set<int>> graph;
    void buildGraph(TreeNode* parent, TreeNode* child) {
        if (parent and child) {
            graph[parent->val].insert(child->val);
            graph[child->val].insert(parent->val);
        }
        if (child->left) buildGraph(child, child->left);
        if (child->right) buildGraph(child, child->right);
    }
    
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        buildGraph(nullptr, root);
        
        queue<int> q; q.push(target->val);
        unordered_set<int> visited; visited.insert(target->val);
        int steps = 0;
        while (steps < k) {
            int nThisLayer = q.size();
            while (nThisLayer--) {
                int node = q.front(); q.pop();
                for (auto neigh : graph[node]) {
                    if (visited.find(neigh) == visited.end()) {
                        q.push(neigh);
                        visited.insert(neigh);
                    }
                }
            }
            ++steps;
        }
        vector<int> ans;
        while (!q.empty()) { ans.push_back(q.front()); q.pop(); }
        return ans;
    }
};
