/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    void _dfs(Node* root, vector<int>& output) {
        if (root == nullptr) {
            return;
        }
        
        if (root->children.empty()) {
            output.push_back(root->val);
            return;
        }

        // otherwise go to the root
        for (Node* temp: root->children) {
            _dfs(temp, output);
        }
        output.push_back(root->val);

    }
    vector<int> postorder(Node* root) {
        vector<int> output;
        _dfs(root, output);

        return output;
    }
};