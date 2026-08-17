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
    vector<vector<int>> res = {};

    int _getHeight(TreeNode* root) {
        if (!root) {
            return 0;
        }

        return 1 + _getHeight(root->left) + _getHeight(root->right);
    }

    void _level(TreeNode* root, int h) {
        if (!root) {
            return ;
        }

        res[h].push_back(root->val);
        _level(root->left, h+1);
        _level(root->right, h+1);
        return ;
    }


    vector<vector<int>> levelOrder(TreeNode* root) {
        int height= _getHeight(root);
        res.resize(height, vector<int>());
        _level(root, 0);
        vector<vector<int>> res2 = {};
        for (vector<int>& temp: res) {
            if (temp.empty() == false) {
                res2.push_back(temp);
            }
        }

        return res2;
    }
};
