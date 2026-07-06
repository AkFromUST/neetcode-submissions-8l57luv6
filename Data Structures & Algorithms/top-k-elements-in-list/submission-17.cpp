class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        unordered_set<int> seen;
        for (int& n: nums) {
            freq[n]++;
        }

        vector<vector<int>> freq_list(nums.size()+1); vector<int> res = {};

        for (int& n: nums) {
            if (seen.contains(n)) {continue;}
            freq_list[freq[n]].push_back(n);
            seen.insert(n);
        }

        int i = freq_list.size()-1; int count = 0;
        while (i >= 0) {
            if (count == k) {return res;}
            
            if (!freq_list[i].empty()) {
                int element = freq_list[i].back();
                freq_list[i].pop_back();
                res.push_back(element);
                count++;
                continue;
            }
            i--;
        }

        return res;
    }
};
