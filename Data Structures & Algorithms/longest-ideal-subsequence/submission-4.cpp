class Solution {
public:
    int _dp(string& s, int& k, int i, char l, vector<vector<int>>& dp) {
        if (i == s.size()) {
            return 0;
        }

        // Map characters safely to column indices 0 to 26
        int col = (l == 'A') ? 26 : (l - 'a');

        if (dp[i][col] != -1) {
            return dp[i][col];
        }

        // Option 1: Not take
        int not_take = _dp(s, k, i + 1, l, dp);

        // Option 2: Take (if valid)
        int take = 0;
        if (l == 'A' || abs(s[i] - l) <= k) {
            take = 1 + _dp(s, k, i + 1, s[i], dp);
        }

        return dp[i][col] = max(take, not_take);
    }
    
    int longestIdealString(string s, int k) {
        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(27, -1));
        
        return _dp(s, k, 0, 'A', dp);
    }
};
