class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int count = 0; int l = 0; int window = 1;

        if (k <= 1) {return 0;}

        for (int r = 0; r < nums.size(); ++r) {
            window *= nums[r];

            while (l <= r && window >= k) {
                window = window / nums[l];
                l++;
            }

            count += (r - l + 1);
        }

        return count;
    }
};