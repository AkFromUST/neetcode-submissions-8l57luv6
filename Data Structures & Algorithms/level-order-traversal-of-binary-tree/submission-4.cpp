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
    
    vector<vector<int>> res;

    int _getDepth(TreeNode* root, int level) {
        if (!root) {
            return level;
        }

        return max(_getDepth(root->left, level + 1), _getDepth(root->right, level + 1));
    }

    void _dfs(TreeNode* root, int level, vector<vector<int>>& res) {
        if (!root) {
            return;
        }

        _dfs(root->left, level + 1, res);
        _dfs(root->right, level + 1, res);
        
        if (root) {
            res[level].push_back(root->val);
        }
        return;
    }

    vector<vector<int>> levelOrder(TreeNode* root) {
        // get me the max depth
        int depth = 0;

        depth = _getDepth(root, 0);

        vector<vector<int>> res = {};
        for (int i = 0; i < depth; ++i) {res.push_back({});}

        _dfs(root, 0, res);

        return res;
    }
};
