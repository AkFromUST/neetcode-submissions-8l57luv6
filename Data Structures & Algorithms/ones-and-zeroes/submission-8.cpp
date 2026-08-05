class Solution {
public:
    
    vector<int> _newCount(vector<int>& count, string& str) {
        for (char& c: str) {
            count[c-'0']++;
        }
        return count;
    }
    
    int _dp(vector<string>& strs, int m, int n, int i, vector<int> count, vector<vector<vector<int>>>& cache) {
        
        // end case. No more strs that fulfills the condition from here.
        if (i >= strs.size()) {
            return 0;
        }

        // if the cache exist. Take it
        int rem_m = m - count[0]; int rem_n = n - count[1];
        if (cache[i][rem_m][rem_n] != -1) {return cache[i][rem_m][rem_n]; }

        //take or not take
        int take = 0; int not_take = 0;

        // dont add anything from this iteration
        not_take = _dp(strs, m, n, i+1, count, cache);

        // update count since we are taking
        count = _newCount(count, strs[i]);
        if ((count[0] <= m && count[1] <= n)) {
            take = 1 + _dp(strs, m,n, i+1, count, cache);
        }
        
        cache[i][rem_m][rem_n] = max(take, not_take);

        return cache[i][rem_m][rem_n];
    }

    
    int findMaxForm(vector<string>& strs, int m, int n) {
        // adding the cache. Two things to look for. The current index and the prevStr we took
        vector<vector<vector<int>>> cache(strs.size(), vector<vector<int>>(m+1, vector<int>(n+1,-1)));
        
        vector<int> count(2,0); return _dp(strs, m, n, 0, count, cache);
    }
};