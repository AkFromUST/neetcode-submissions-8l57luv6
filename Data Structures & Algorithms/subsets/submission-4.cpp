class Solution {
public:
    vector<vector<int>> ans;
    
    void _dfs(vector<int>& currsubs, vector<int>& nums , int index, int n) {
        // end case, index at the end of the nums
        if (index >= n) {
            ans.push_back(currsubs);
            return;
        }

        //take this index?
        currsubs.push_back(nums[index]);
        _dfs(currsubs, nums, index + 1, n);        

        // Remove it now
        currsubs.pop_back();
        _dfs(currsubs, nums, index + 1, n);
    }
    
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size(); vector<int> placeholder;
        _dfs(placeholder, nums, 0, n);
        return ans;

    }
};
