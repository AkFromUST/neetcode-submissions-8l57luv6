class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        // simple

        int state = 0; int l = 0; int min_len = nums.size()+1;
        
        for (int r = 0; r < nums.size(); r++) {
            state += nums[r];

            while (state >= target) {
                min_len = min(min_len, r-l+1);
                state -= nums[l]; l++;
            }
        }

        if (min_len == nums.size()+1) { return 0;} return min_len;
    }
};