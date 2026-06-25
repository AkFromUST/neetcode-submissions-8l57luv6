class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count = 0; int n = nums.size();

        for (int i = 0; i < n; ++i) {
            if (nums[i] != val) {
                int temp = nums[count]; nums[count] = nums[i]; nums[i] = temp;
                count++;
            }
        }
        return count;
    }
};