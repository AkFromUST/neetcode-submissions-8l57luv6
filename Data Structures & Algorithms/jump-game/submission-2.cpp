class Solution {
public:
    
    bool _dp(vector<int>& nums, int i, vector<int>& dp) {
        if (i >= nums.size() - 1) {
            return true;
        } 
        
        if (dp[i] != -2) {
            return dp[i];
        }
        
        bool res = false; int j = i+1;
        while (j < nums.size() && j <= (nums[i] + i)) {
            res = res || _dp(nums, j, dp);
            j++;
        }
        return dp[i] = res;
    }
    
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        vector<int>dp(n+1, -2);
        return _dp(nums, 0, dp);
    }
};
