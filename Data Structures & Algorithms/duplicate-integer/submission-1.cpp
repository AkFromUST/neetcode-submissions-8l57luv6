class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> res = {};

        for (auto num: nums) {
            res.insert(num);
            cout << num << endl;
        }

        if (res.size() != nums.size()) {return true;} else {return false;}
    }
};
