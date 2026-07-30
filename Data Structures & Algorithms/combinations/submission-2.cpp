class Solution {
public:
    void _dfs(vector<vector<int>>& res, int i, vector<int>& comb, int k, int n) {
        if (i > n) {
            if (comb.size() == k) {
                res.push_back(comb);
            } return ;
        }

        // take
        comb.push_back(i);
        _dfs(res, i+1, comb, k, n);
        comb.pop_back();
        _dfs(res, i+1, comb, k, n);

        return ;
    }
    
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res = {}; vector<int> comb = {};
        _dfs(res, 1, comb, k, n);

        return res;
    }
};