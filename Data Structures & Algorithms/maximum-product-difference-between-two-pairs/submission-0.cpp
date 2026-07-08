class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        sort(nums.begin(), nums.end()); int n = nums.size();

        int res1 = nums[n-1] * nums[n-2]; int res2 = nums[0] * nums[1];
        return res1 - res2;
    }
};