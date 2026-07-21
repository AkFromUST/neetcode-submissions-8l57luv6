class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        // get the starting and ending of this range. Both are (Ologn)

        if (nums.empty()) { return {-1,-1}; }

        int start = -1; int l = 0; int r = nums.size() - 1;

        while (l <= r) {
            int mid = l + (r-l)/2;
             
            if (nums[mid] >= target) {
                r = mid - 1;
            }
            if (nums[mid] < target) {
                l = mid + 1;
            }
        }

        start = l;
        int end = -1; r = nums.size()-1;

        while (l <= r) {
            int mid = l + (r-l)/2;

            if (nums[mid] <= target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        end = r;
        // take the max
        
        if (start >= nums.size() || end < 0) { return {-1,-1}; } 
        if (nums[start] == target) {
            return {start, end};
        } return {-1,-1};

    }
};