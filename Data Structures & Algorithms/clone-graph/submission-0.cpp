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
    
    Node* _dfs(Node* node, unordered_map<Node*, Node*>& seen) {
        if (!node) {
            return nullptr;
        }

        if (seen.contains(node)) {
            return seen[node];
        }

        Node* new_root = new Node(node->val);
        seen[node] = new_root;
        for (Node* old_nei: node->neighbors) {
            new_root->neighbors.push_back(_dfs(old_nei, seen));
        }

        return new_root;
        
    }
    
    Node* cloneGraph(Node* node) {

        if (!node) {
            return nullptr;
        }

        unordered_map<Node*, Node*> seen = {};
        _dfs(node, seen);
        return seen[node];
    }
};
