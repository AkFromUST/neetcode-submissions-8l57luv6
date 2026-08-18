class Solution {
public:

    vector<int> _count(string& str) {
        vector<int> res(2,0);
        for (char& c: str) {
            res[c-'0']++;
        }
        return res;
    }

    
    // I remember this. This is 2D DP
    int _dp(vector<string>& strs, int m, int n, int i, int ones, int zeroes,vector<vector<vector<int>>>& dp) {
        if (i == strs.size()) {
            return 0;
        }

        if (dp[i][ones][zeroes] != -1) { return dp[i][ones][zeroes]; }

        int take = 0; int dont_take = 0;
        dont_take = _dp(strs, m, n, i+1, ones, zeroes, dp);

        vector<int> count = _count(strs[i]);
        if ((ones + count[1]) <= n && (zeroes + count[0]) <= m) {
            take = 1 + _dp(strs, m, n, i+1, ones + count[1], zeroes + count[0], dp);
        }

        return dp[i][ones][zeroes] = max(take, dont_take);
    }
    
    
    int findMaxForm(vector<string>& strs, int m, int n) {
        int s = strs.size(); vector<vector<vector<int>>> dp(s, vector<vector<int>>(n+1, vector<int>(m+1, -1)));

        return _dp(strs, m, n, 0, 0, 0, dp);
    }
};