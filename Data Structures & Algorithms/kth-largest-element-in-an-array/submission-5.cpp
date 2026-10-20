class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        vector<int> counter(2001, 0);

        for (int& n: nums) {
            counter[n + 1000]++;
        }
        int count = 0; int i = 2000;
        while (i > 0) {
            if (count == k) {
                return (i - 1000);
            }
            
            if (counter[i] > 0) {
                count++;
                counter[i]--;
                continue;
            }
            else if (counter[i] == 0) {
                i--;
            }
        }
        return -1;
    }
};
