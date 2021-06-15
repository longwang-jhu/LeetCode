// https://leetcode.com/problems/clone-graph/

// Given a reference of a node in a connected undirected graph.

// Return a deep copy (clone) of the graph.

// Each node in the graph contains a value (int) and a list (List[Node]) of its
// neighbors.

////////////////////////////////////////////////////////////////////////////////

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == nullptr) return node;
        unordered_map<Node*, Node*> copies; // copies[old node] = copied node
        copies[node] = new Node(node->val);
        
        queue<Node*> todo; todo.push(node);
        while (!todo.empty()) {
            Node* curr = todo.front(); todo.pop();
            for (Node* neigh : curr->neighbors) {
                if (copies.find(neigh) == copies.end()) {
                    copies[neigh] = new Node(neigh->val);
                    todo.push(neigh);
                }
                copies[curr]->neighbors.push_back(copies[neigh]);
            }
        }
        return copies[node];
    }
};
