class Solution {
public:
    int specialArray(vector<int>& nums) {
        int max = *max_element(nums.begin(), nums.end()); vector<int> freq(max+1, 0);
        
        // Now we can just iterate from the end to the start. 
        for (int& n: nums) { freq[n]++; }
        
        // for (auto& e: freq) { cout << e << " ";}
        
        // Reverse iteration pls
        int total_bigger = 0;
        for (int i = max; i > 0; --i) {
            // index is the number, freq[index] is the freq
            total_bigger += freq[i];
            if (total_bigger == i) { return i; }
        }
        return -1;
    }
};