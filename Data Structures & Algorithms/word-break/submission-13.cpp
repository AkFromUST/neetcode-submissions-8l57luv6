class Solution {
public:
    
    bool _dp(string s, unordered_set<string>& wordDict, string curr, int i, int l, vector<vector<int>>& dp) {
        // cout << curr << endl;
        if (i == s.size()) {
            // check if it contains or not
            if (wordDict.contains(curr)) return true;
            return false;
        }

        if (dp[i][l] != -1) { return dp[i][l]; }

        // break here or not break
        bool res = false; 
        if (wordDict.contains(curr)) {
            string temp = ""; temp += s[i];
            res = res || _dp(s, wordDict, temp, i+1, i, dp);
        }

        // otherwise we break it here
        curr += s[i];
        res = res || _dp(s, wordDict, curr, i+1, l, dp);

        return dp[i][l] = res;
    }
    
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> word_dict(wordDict.begin(), wordDict.end());
        vector<vector<int>> dp(s.size()+1, vector<int> (s.size() + 1, -1));
        return _dp(s, word_dict, "", 0, 0, dp);
    }
};
