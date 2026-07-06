class Solution {
public:
    vector<vector<int>> all_subsets = {};
    
    void _dfs(int index, int n, vector<int>& subs, vector<int> &nums) {
        
        if (index == n) {
            all_subsets.push_back(subs);
            return ;
        }
        
        subs.push_back(nums[index]);
        _dfs(index+1, n, subs, nums);

        while ((index+1< n) && (nums[index] == nums[index+1])) { index++;}

        subs.pop_back();
        _dfs(index+1, n, subs, nums);
        return ;
    }
    
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        int n = nums.size(); vector<int> temp = {};
        sort(nums.begin(), nums.end());
        _dfs(0, n, temp, nums);
        
        return all_subsets;
        
    }
};
