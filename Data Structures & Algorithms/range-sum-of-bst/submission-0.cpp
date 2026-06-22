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
    int sum = 0;
    void _dfs(TreeNode* root, int low, int high) {
        if (root == nullptr) {
            return;
        }

        // call on children
        if (low <= root->val && high >= root->val) {
            sum += root->val;
        }

        _dfs(root->left, low, high);
        _dfs(root->right,low, high);
    }

    int rangeSumBST(TreeNode* root, int low, int high) {
        _dfs(root,low, high);
        return sum;
    }
};