class Solution {
public:
    
    int _dfs(vector<int>& nums, int i, int target, vector<int>& cache) {
        if (i == nums.size() || target < 0) {
            return 0;
        }

        if (cache[target] != -1) { return cache[target]; }
        
        if (target == 0) { return 1; }

        int res = 0;

        for (int i = 0; i < nums.size(); ++i) {
            res += _dfs(nums, i, target - nums[i], cache);
        }

        return cache[target] = res;
    }
    
    int combinationSum4(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end()); vector<int> cache(target + 1, -1);
        cache[0] = 1;
        
        return _dfs(nums, 0, target, cache);
    }

// NO DP

    // int _dfs(vector<int>& nums, int i, int target) {
    //     if (i == nums.size() || target < 0) {
    //         return 0;
    //     }
        
    //     if (target == 0) { return 1; }

    //     int res = 0;

    //     for (int i = 0; i < nums.size(); ++i) {
    //         if (nums[i] > target) { return res; }
    //         res += _dfs(nums, i, target - nums[i]);
    //     }

    //     return res;
    // }
    
    // int combinationSum4(vector<int>& nums, int target) {
    //     sort(nums.begin(), nums.end()); vector<vector<int>> cache(nums.size(), vector<int>(target+1, -1));
        
    //     return _dfs(nums, 0, target);
    // }
};