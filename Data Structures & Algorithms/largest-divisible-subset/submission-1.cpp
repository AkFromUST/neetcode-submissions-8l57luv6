class Solution {
public:
    
    int max_len = 0;
    vector<int> res = {};
    
    void _dfs(vector<int> &nums, int n, vector<int>& subset, int i) {
        if (i >= n) {
            // check if this subset is higher or not
            if (max_len < subset.size()) {
                res = subset;
                max_len = subset.size();
            }
            return;
        }

        // take or not
        _dfs(nums, n, subset, i+1);

    
        if (subset.empty() || nums[i] % subset.back() == 0) {
            // take this
            subset.push_back(nums[i]);
            _dfs(nums, n, subset, i+1);
            subset.pop_back();
        }

        return;
    }
    
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(), nums.end()); vector<vector<int>> cache = {}; int n = nums.size(); vector<int> temp = {};
        _dfs(nums, n, temp, 0);
        return res;
    }
};