class Solution {
public:
    int minOperations(vector<int>& nums) {
        unordered_map<int, int> counter = {};        
        for (const int& n: nums) { counter[n]++; }

        int count = 0;
        for (const auto& [val, freq]: counter) {
            if (freq == 1) {return -1;}

            // otherwise. Any number can be expressed as a linear expression of 2s and 3s.
            count += (freq + 2) / 3;
        }
        return count;
    }
};