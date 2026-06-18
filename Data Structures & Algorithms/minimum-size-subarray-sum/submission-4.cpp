class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int window = 0; int l = 0; int r = 0; int n = nums.size(); int minsubs = n + 1; 

        // make the first window

        while (r < n) {

            window += nums[r];
            
            // cout << "Window at: " << window << "\t r: " << r << endl;

            // window >= target
            while (window >= target) {
                minsubs = min(minsubs, r-l+1);
                window -= nums[l]; l++;
            }
            r++;
            // cout << "\tWindow at: " << window << "\tl: " << l << "\tr: " << r << endl;
        }

        if (minsubs == n+1) {  return 0;}
        return minsubs;
    }
};