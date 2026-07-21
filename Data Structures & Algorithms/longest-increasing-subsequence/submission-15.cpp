class Solution {
public:

    // then you can think of putting top-down here. 
    vector<vector<int>> cache;

    int _dfs(int i, vector<int>& nums, int previ) {
        if (i >= nums.size()) { return 0; }

        if (cache[i][previ + 1] != -1) { return cache[i][previ+1]; }
    
        // not take
        int take = 0; int notTake = 0;
        notTake = _dfs(i+1, nums, previ);

        if ( previ == -1 || nums[i] > nums[previ]) {
            take = 1 + _dfs(i+1, nums, i);
        }

        return cache[i][previ + 1] = max(take, notTake);

    }
    
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size(); cache.assign(n, vector<int> (n+1, -1));        
        return _dfs(0,nums, -1);
    }
};
