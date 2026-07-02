class Solution {
public:
    
    vector<vector<int>> res;

    void _dfs(int index, int n, vector<int>& temp, vector<int> &nums) {
        if (index >= n) {
            res.push_back(temp);
            return ;
        }

        // take or not take
        _dfs(index + 1, n, temp, nums);
        temp.push_back(nums[index]); _dfs(index+1, n, temp, nums);
        temp.pop_back();
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> temp = {};
        _dfs(0, nums.size(), temp, nums);
        return res;
    }
};
