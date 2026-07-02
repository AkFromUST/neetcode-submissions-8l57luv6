class Solution {
public:
    
    vector<vector<int>> res;

    void _dfs(int index, int n, vector<int> temp, vector<int> &nums) {
        if (index >= n) {
            res.push_back(temp);
            return ;
        }

        // take or not take
        _dfs(index + 1, n, temp, nums);
        
        temp.push_back(nums[index]); _dfs(index+1, n, temp, nums);
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        _dfs(0, nums.size(), {}, nums);
        return res;
    }
};
