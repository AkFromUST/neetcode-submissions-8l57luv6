class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        vector<int> counts(2001, 0);

        for (int& n: nums) { counts[n+1000]++; }

        // for (int i = 0; i < 2001;i++) {cout << counts[i] << " ";}

        int r = 2000; int count = 1;

        while (r >= 0) {
            while (counts[r] > 0) {
                if (count == k) { return r -1000; }
                count++;
                counts[r]--;
            }
            r -= 1;
        }

        return 0;
    }
};
