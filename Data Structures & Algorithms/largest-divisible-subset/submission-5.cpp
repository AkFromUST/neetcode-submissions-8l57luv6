class Solution {
public:
    
    vector<vector<vector<int>>> cache;
    
    vector<int> _dfs(int i, int previ, vector<int>& nums) {
        if (i >= nums.size()) {
            return {};
        }

        if (!cache[i][previ+1].empty()) {
            return cache[i][previ+1];
        }

        vector<int> take = {}; vector<int> notTake = {};

        notTake = _dfs(i+1, previ, nums);
        if (previ == -1 || nums[i] % nums[previ] == 0) {
            // create a temp vector
            take = {nums[i]};
            vector<int> temp = _dfs(i+1, i, nums);
            take.insert(take.end(), temp.begin(), temp.end());
        }
        
        if (notTake.size() > take.size()) {
            take = notTake;
        }
        return cache[i][previ + 1] = take;
    }
    
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(), nums.end()); int n = nums.size();
        cache = vector<vector<vector<int>>> (n, vector<vector<int>>(n+1));
        return _dfs(0, -1, nums);
    }
};