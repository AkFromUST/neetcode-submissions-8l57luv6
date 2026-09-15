class Solution {
public:
    vector<int> partitionLabels(string s) {
        // store the last index for that char.
        vector<int> all_chars(26,0);
        int l = 0; int n = s.size();

        for (int r = 0; r < n; ++r) { all_chars[s[r] - 'a'] = r; }

        vector<int> res = {}; int last_index = 0;

        for (int r = 0; r < n; ++r) {
            // what is THIS char's last index
            last_index = max(last_index, all_chars[s[r] - 'a']);
            
            // storing this partition
            if (last_index == r) {
                res.push_back(r-l+1);
                l = r+1;
            }
        }

        return res;
    }
};
