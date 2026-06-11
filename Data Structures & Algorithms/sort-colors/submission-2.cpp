class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int> freq(3, 0); for (int n: nums) { freq[n]++; }
        int index = 0;
        for (int i = 0; i < freq.size(); i++) {
            int n = freq[i];
            for (int j = 0; j < n; j++) {
                nums[index] = i;
                index++;
            }
        }
    }
};