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
    unordered_set<int> allNodes; TreeNode* lca = nullptr; int first = 0;
    
    bool _dfs(TreeNode* root, int target) {
        if (!root) {
            return false;
        }

        if (root->val == target) {
            allNodes.insert(root->val);
            return true;
        }

        
        if (_dfs(root->left, target)) {
            allNodes.insert(root->val);
            return true;
        }

        if (_dfs(root->right, target)) {
            allNodes.insert(root->val);
            return true;
        }

        return false;
    }

    TreeNode* _LCA(TreeNode* root, int target) {
        if (!root) {
            return nullptr;
        }

        cout << root->val << " ";

        if (root->val == target) {
            if (allNodes.contains(root->val)) {
                if (first == 0) {
                    lca = root;
                    first++;
                }
            } return root;
        }

        
        if (_LCA(root->left, target)) {
            if (allNodes.contains(root->val)) {
                if (first == 0) {
                    lca = root;
                    first++;
                }
            } return root;
        }

        if (_LCA(root->right, target)) {
            if (allNodes.contains(root->val)) {
                if (first == 0) {
                    lca = root;
                    first++;
                }
            }
            return root;
        }

        return nullptr;
    }
    
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        _dfs(root, p->val);

        cout << " " << endl;
        for (const auto& e: allNodes) {
            cout << e << " ";
        }

        _LCA(root, q->val);

        if (lca != nullptr) {
            return lca;
        } return root;
        
    }
};
