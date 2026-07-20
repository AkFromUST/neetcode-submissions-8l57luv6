class Solution {
public:
    
    // int max_len = 0;
    // vector<int> res = {};
    // vector<vector<vector<int>>> cache = {};
    
    // void _dfs(vector<int> &nums, int n, vector<int>& subset, int i) {
    //     if (i >= n) {
    //         // check if this subset is higher or not
    //         if (max_len < subset.size()) {
    //             res = subset;
    //             max_len = subset.size();
    //         }
    //         return;
    //     }

    //     // take or not
    //     _dfs(nums, n, subset, i+1);

    //     if (subset.empty() || nums[i] % subset.back() == 0) {
    //         // take this
    //         subset.push_back(nums[i]);
    //         _dfs(nums, n, subset, i+1);
    //         subset.pop_back();
    //     }

    //     return;
    // }
    
    // vector<int> largestDivisibleSubset(vector<int>& nums) {
    //     sort(nums.begin(), nums.end()); vector<vector<int>> cache = {}; int n = nums.size(); vector<int> temp = {};
    //     _dfs(nums, n, temp, 0);
    //     return res;
    // }

    vector<vector<vector<int>>> cache = {};
    
    vector<int> _dfs(vector<int> &nums, int n, int i, int previndex) {
        if (i >= n) { return {}; }

        // because starting is at -1. So doing +1 makes the starting at 0
        if (!cache[i][previndex+1].empty()) {return cache[i][previndex+1];}

        // take or not
        vector<int> temp2 = _dfs(nums, n, i+1, previndex);
        vector<int> temp = {};
        if (previndex == -1 || nums[i] % nums[previndex] == 0) {
            // add it to the subset
            temp.push_back(nums[i]);
            vector<int> take = _dfs(nums, n, i+1, i);
            temp.insert(temp.end(), take.begin(), take.end());
            if (temp.size() > temp2.size()) {temp2 = temp;}
        }

        return cache[i][previndex+1] = temp2;
    }
    
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(), nums.end()); int n = nums.size();
        cache = vector<vector<vector<int>>> (n, vector<vector<int>> (n+1));
        return _dfs(nums, n, 0, -1);
    }
};