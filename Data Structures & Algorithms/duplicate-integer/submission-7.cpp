class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        using namespace std;
        unordered_set<int> seen;
        
        for (auto num: nums) {
            if (seen.count(num) != 1) {
                seen.insert(num);
            } else {
                return true;
            }
        }

        return false;
    }
};