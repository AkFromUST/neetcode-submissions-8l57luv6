class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int window = 0; int l = 0; int res = INT_MAX;

        for (int r = 0; r < nums.size(); ++r) {
            window += nums[r];

            while (window >= target) {
                res = min(res, r-l+1);
                window -= nums[l];
                l++;
            }
        }

        if (res == INT_MAX) {
            return 0;
        } return res;
    }
};