class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        
        if (strs.size() == 1) {
            return strs[0];
        }
        
        int smallest = INT_MAX;
        for (int i = 0; i < strs.size(); ++i) {
            smallest = min(smallest, (int) strs[i].size());
        }
        int r = 0; string temp = ""; cout << smallest << endl;

        while (r < smallest) {
            temp += strs[0][r];
            for (auto& s: strs) {
                if (s[r] != temp[r]) {
                    return s.substr(0, r);
                }
            }
            r++;
        }

        if (strs[0][0] != strs[1][0]) {return "";}
        return temp;
    }
};