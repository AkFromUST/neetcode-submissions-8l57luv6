class Solution {
public:
    vector<int> partitionLabels(string s) {
        // store the last index for that char.
        unordered_map<char, int> all_chars = {};
        int l = 0; int n = s.size();

        for (int r = 0; r < n; ++r) { all_chars[s[r]] = r; }

        vector<int> res = {}; int last_index = 0;

        for (int r = 0; r < n; ++r) {
            // what is THIS char's last index
            last_index = max(last_index, all_chars[s[r]]);
            
            // storing this partition
            if (last_index == r) {
                res.push_back(r-l+1);
                l = r+1;
            }
        }

        return res;
    }
};
