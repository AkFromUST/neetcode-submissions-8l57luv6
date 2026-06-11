class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> freq;
        int most_freq = 0; int most_freq_e = 0;
        for (auto& n: nums) {
            freq[n]++;
            if (freq[n] > most_freq) { 
                most_freq = freq[n];
                most_freq_e = n;
            }
        }

        return most_freq_e;
    }
};