class Solution {
public:
    
    int max = (1000 * 100) + 1;

    int _dp(vector<int>& nums, vector<vector<int>>& dp, int i, int previ) {
        if (i >= (nums.size() - 1)) {
            return 0;
        }

        if (nums[i] == 0) {return max;}
        
        if (dp[i][previ + 1] != -1) {
            return dp[i][previ + 1];
        }

        int steps = max;
        for (int j = 1; j <= nums[i]; j++) {
            int local_steps = _dp(nums, dp, j+i, i);
            if (local_steps != max) {steps = min(steps, 1 + local_steps);}
        }

        return dp[i][previ+1] = steps;
    }
    
    int jump(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(n+1, -1));
        return _dp(nums, dp, 0, -1);
    }
};
