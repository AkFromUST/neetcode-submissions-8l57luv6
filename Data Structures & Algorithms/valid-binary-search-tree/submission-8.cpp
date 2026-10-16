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
    bool _isvalid(TreeNode* root, int low, int max) {
        if (!root) {
            return true;
        }
        if (root-> val > low && root->val < max) {
            return true && (_isvalid(root->left, low, root->val) && _isvalid(root->right, root->val, max));
        } else {
            return false;
        }
    }

    bool isValidBST(TreeNode* root) {
        int low = -1e9 - 1; int max = 1e7+1;
        return _isvalid(root, low, max);
    }
};
