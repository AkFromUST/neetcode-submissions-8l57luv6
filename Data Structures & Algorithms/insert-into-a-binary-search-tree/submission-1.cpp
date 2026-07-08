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
    TreeNode* _dfs(TreeNode* root, int val) {
        TreeNode* returned = nullptr;
        
        if (!root) {
            // that means the val must be inserted here
            cout << "Reached" << endl;
            returned = new TreeNode(val, nullptr, nullptr);
            return returned;
        }

        

        if (root->val < val) {
            cout << "going right" << endl;
            // that means that val is above this root
            returned = _dfs(root->right, val);
            if (returned) {root->right = returned;}
            return nullptr;
        }
        if (root->val > val) {
            // go left
            returned = _dfs(root->left, val);
            if (returned) {root->left = returned;}
            return nullptr;
        }

        // return returned;
    }
    
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (!root) {
            root = new TreeNode(val, nullptr, nullptr);
            return root;
        }
        
        _dfs(root, val);
        return root;      
    }
};