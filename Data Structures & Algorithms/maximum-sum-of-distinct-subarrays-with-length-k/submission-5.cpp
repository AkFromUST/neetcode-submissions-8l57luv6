class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        // for sure sliding window.

        int l = 0; long long max_len = 0; unordered_map<int, int> window; int n = nums.size(); long long window_len = 0; long long window_sum = 0; bool unique = true;

        for (int r = 0; r < n; ++r) {
            window[nums[r]]++;
            if (window[nums[r]] > 1) unique = false;
            window_len++; window_sum += nums[r];

            while (l <= r && (window_len > k || unique == false)) {
                window[nums[l]]--; window_sum -= nums[l];
                l++; window_len--;
                // addition of nums[r] will cause the unique to become false. So we must look for nums[r] to become unique again.
                if (window[nums[r]] == 1) unique = true;
            }

            if (window_len == k && unique) {
                cout << "l: " << l << "\tr: " << r << endl;
                max_len = (long long) max(max_len, window_sum);
            }
        }

        return (long long) max_len;
    }
};
