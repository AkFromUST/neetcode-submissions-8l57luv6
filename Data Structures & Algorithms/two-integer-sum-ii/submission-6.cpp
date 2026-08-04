class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0; int r = numbers.size() - 1;

        while (l < r) {
            int tempsum = numbers[r] + numbers[l];

            if (tempsum > target) {
                r--;
            }
            if (tempsum < target) {
                l++;
            }
            if (tempsum == target) {
                return {l+1,r+1};
            }
        }
        return vector<int> {-1,-1};
    }
};
