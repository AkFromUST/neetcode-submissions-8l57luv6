class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int l = 0; long long window = 0; int n = nums.size(); int freq = 1;

        for (int r = 1; r < n; r++) {

            window += (long long)((nums[r] - nums[r-1]) * (r-l));

            while (window > k) {
                window -= (nums[r] - nums[l]);
                cout << "\t" << window << endl;
                l++;
            }

            cout << r << " " << l << endl;

            freq = max(freq, r-l+1);
        }
        return freq;
    }
};