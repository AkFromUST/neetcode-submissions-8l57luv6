class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> hashmap;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            
            //init vars
            int curr = nums[i];
            int diff = target - curr;

            if (hashmap.count(diff)) {
                return {hashmap[diff], i};
            }

            hashmap[curr] = i;
        }
        return {};
    }
};
