class Solution {
    
    vector<string> ans;

public:
    void _backtracking(string& s, int i, unordered_set<string>& wordDict, vector<string>& res) {
        if (i == s.size()) {
            ans.push_back(join(res));
            return ; //something
        }

        for (int j = i; j < s.size(); ++j) {
            string substring = s.substr(i, j-i+1);
            if (wordDict.contains(substring)) {
                res.push_back(substring);
                _backtracking(s, j+1, wordDict, res);
                res.pop_back();
            }
        }
    }

    string join(const vector<string>& words) {
        ostringstream oss;
        for (int i = 0; i < words.size(); ++i) {
            if (i > 0) oss << " ";
            oss << words[i];
        }
        return oss.str();
    }
    
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        vector<string> res = {};
        _backtracking(s, 0, wordSet, res);
        return ans;
    }
};