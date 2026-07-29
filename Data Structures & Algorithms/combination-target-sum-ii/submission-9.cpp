class Solution {
public:
    vector<vector<int>> res = {};

    void _dfs(vector<int>& candidates, int target, int index, int sum, vector<int>& subset) {
        if (index >= candidates.size()) {
            if (sum == target) {res.push_back(subset);}
            return ;
        }

        if (sum > target) {return;}

        subset.push_back(candidates[index]);
        _dfs(candidates, target, index + 1, sum + candidates[index], subset);
        subset.pop_back();
        //take or not take
        
        while (index + 1 < candidates.size() && candidates[index] == candidates[index + 1]) {
            index++;
        }
        _dfs(candidates, target, index + 1, sum, subset);

    }
    
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end()); vector<int> subset = {};
        _dfs(candidates, target, 0, 0, subset);
        return res;
    }
};
