class Solution {
public:
    
    bool _dp(vector<int>& nums, int i, int previ, vector<vector<int>>& dp) {
        if (i >= nums.size() - 1) {
            return true;
        } 
        
        if (dp[i][previ+1] != -2) {
            return dp[i][previ + 1];
        }
        
        bool res = false; int j = i+1;
        while (j < nums.size() && j <= (nums[i] + i)) {
            res = res || _dp(nums, j, i, dp);
            j++;
        }
        return dp[i][previ + 1] = res;
    }
    
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n+1, vector<int>(n+1, -2));
        return _dp(nums, 0, -1, dp);
    }
};
